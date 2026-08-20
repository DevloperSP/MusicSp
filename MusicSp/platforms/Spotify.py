import re
from typing import Union
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from py_yt import VideosSearch
import config


class SpotifyAPI:
    def __init__(self):
        self.regex = r"^(https:\/\/open.spotify.com\/)(.*)$"
        self.client_id = config.SPOTIFY_CLIENT_ID
        self.client_secret = config.SPOTIFY_CLIENT_SECRET
        if config.SPOTIFY_CLIENT_ID and config.SPOTIFY_CLIENT_SECRET:
            try:
                self.client_credentials_manager = SpotifyClientCredentials(
                    self.client_id, self.client_secret
                )
                self.spotify = spotipy.Spotify(
                    client_credentials_manager=self.client_credentials_manager
                )
            except Exception:
                self.spotify = None
        else:
            self.spotify = None

    async def valid(self, link: str):
        if re.search(self.regex, link):
            return True
        else:
            return False

    async def track(self, link: str):
        if not self.spotify:
            return False
        try:
            track = self.spotify.track(link)
            info = track["name"]
            for artist in track["artists"]:
                fetched = f' {artist["name"]}'
                if "Various Artists" not in fetched:
                    info += fetched
            results = VideosSearch(info, limit=1)
            res = await results.next()
            if not res or not res.get("result"):
                return False
            for result in res["result"]:
                ytlink = result["link"]
                title = result["title"]
                vidid = result["id"]
                duration_min = result["duration"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            track_details = {
                "title": title,
                "link": ytlink,
                "vidid": vidid,
                "duration_min": duration_min,
                "thumb": thumbnail,
            }
            return track_details, vidid
        except Exception:
            return False

    async def playlist(self, url):
        if not self.spotify:
            return [], None
        try:
            playlist = self.spotify.playlist(url)
            playlist_id = playlist["id"]
            results = []
            for item in playlist["tracks"]["items"]:
                music_track = item["track"]
                if not music_track:
                    continue
                info = music_track["name"]
                for artist in music_track.get("artists", []):
                    fetched = f' {artist["name"]}'
                    if "Various Artists" not in fetched:
                        info += fetched
                results.append(info)
            return results, playlist_id
        except Exception:
            return [], None

    async def album(self, url):
        if not self.spotify:
            return [], None
        try:
            album = self.spotify.album(url)
            album_id = album["id"]
            results = []
            for item in album["tracks"]["items"]:
                info = item["name"]
                for artist in item.get("artists", []):
                    fetched = f' {artist["name"]}'
                    if "Various Artists" not in fetched:
                        info += fetched
                results.append(info)
            return results, album_id
        except Exception:
            return [], None

    async def artist(self, url):
        if not self.spotify:
            return [], None
        try:
            artistinfo = self.spotify.artist(url)
            artist_id = artistinfo["id"]
            results = []
            artisttoptracks = self.spotify.artist_top_tracks(url)
            for item in artisttoptracks.get("tracks", []):
                info = item["name"]
                for artist in item.get("artists", []):
                    fetched = f' {artist["name"]}'
                    if "Various Artists" not in fetched:
                        info += fetched
                results.append(info)
            return results, artist_id
        except Exception:
            return [], None
