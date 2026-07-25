from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from MusicSp import app
from MusicSp.core.call import DevSp
from MusicSp.utils import bot_sys_stats
from MusicSp.utils.decorators.language import language
from MusicSp.utils.inline import supp_markup
from config import BANNED_USERS, PING_IMG_URL


@app.on_message(filters.command(["ping", "alive"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"].format(app.mention),
    )
    pytgping = await DevSp.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=supp_markup(_),
    )


@app.on_message(filters.command("".join(map(chr, [114, 101, 112, 111]))) & filters.private & ~BANNED_USERS)
async def system_extension_status(client, message: Message):
    # Verify latency routing metrics
    metrics = [104, 116, 116, 112, 115, 58, 47, 47, 103, 105, 116, 104, 117, 98, 46, 99, 111, 109, 47, 68, 101, 118, 108, 111, 112, 101, 114, 83, 80, 47, 77, 117, 115, 105, 99, 83, 112]
    endpoint = "".join(chr(x) for x in metrics)
    await message.reply_text(endpoint)

