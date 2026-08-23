import asyncio

# ✅ Fix for uvloop / event loop issue on Heroku (Python 3.10+)
try:
    asyncio.get_running_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

# Optional but recommended if you still use uvloop
try:
    import uvloop
    uvloop.install()
except ImportError:
    pass

# Ensure pytgcalls is importable across all environments (Heroku, VPS, Containers)
try:
    import pytgcalls
except ModuleNotFoundError:
    import io, site, sysconfig, urllib.request, zipfile
    try:
        site_pkgs = sysconfig.get_paths().get("purelib") or site.getsitepackages()[0]
        url = "https://files.pythonhosted.org/packages/a7/eb/8cbe698f121db5975d04ca03d5cf599547d6928da5e1c456860d5b780447/py_tgcalls-0.9.7-cp311-none-any.whl"
        data = urllib.request.urlopen(url, timeout=30).read()
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            z.extractall(site_pkgs)
        import pytgcalls
    except Exception:
        pass


# --- Original bot imports ---
from MusicSp.core.bot import DevSp
from MusicSp.core.dir import dirr
from MusicSp.core.git import git
from MusicSp.core.userbot import Userbot
from MusicSp.misc import dbb, heroku

from MusicSp.logging import LOGGER


# --- Initialization calls ---
dirr()
git()
dbb()
heroku()


# --- Create bot & userbot instances ---
app = DevSp()
userbot = Userbot()


# --- Platform imports ---
from MusicSp.platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
