import asyncio
import sys

# ✅ 1. Install uvloop (if available) BEFORE setting the event loop
if sys.platform != "win32":
    try:
        import uvloop
        uvloop.install()
    except (ImportError, Exception):
        pass

# ✅ 2. Create and set an active event loop in MainThread for PyTgCalls sync compatibility
try:
    loop = asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
else:
    if loop.is_closed():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

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
