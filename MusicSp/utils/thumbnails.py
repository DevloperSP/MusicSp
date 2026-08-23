# ATLEAST GIVE CREDITS IF YOU STEALING :(((((((((((((((((((((((((((((((((((((
# ELSE NO FURTHER PUBLIC THUMBNAIL UPDATES

import logging
import os
import aiofiles
import aiohttp
from PIL import Image
from py_yt import VideosSearch

import config

logging.basicConfig(level=logging.INFO)

def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage

async def gen_thumb(videoid: str):
    if not videoid or str(videoid).strip().lower() in ("none", "", "null"):
        return config.STREAM_IMG_URL
    try:
        os.makedirs("cache", exist_ok=True)
        if os.path.isfile(f"cache/{videoid}_v4.png"):
            return f"cache/{videoid}_v4.png"

        url = f"https://www.youtube.com/watch?v={videoid}"
        results = VideosSearch(url, limit=1)
        res_data = await results.next()
        thumbnail = None
        if res_data and "result" in res_data and len(res_data["result"]) > 0:
            thumbnail_data = res_data["result"][0].get("thumbnails")
            if thumbnail_data:
                thumbnail = thumbnail_data[0]["url"].split("?")[0]

        if not thumbnail:
            return config.STREAM_IMG_URL

        filepath = f"cache/thumb{videoid}.png"
        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    async with aiofiles.open(filepath, mode="wb") as f:
                        await f.write(await resp.read())

        if not os.path.exists(filepath):
            return config.STREAM_IMG_URL

        youtube = Image.open(filepath)
        background = changeImageSize(1280, 720, youtube)
        background = background.convert("RGB")
        
        try:
            os.remove(filepath)
        except Exception:
            pass
            
        background_path = f"cache/{videoid}_v4.png"
        background.save(background_path)
        return background_path

    except Exception as e:
        logging.error(f"Error generating thumbnail for video {videoid}: {e}")
        return config.STREAM_IMG_URL
