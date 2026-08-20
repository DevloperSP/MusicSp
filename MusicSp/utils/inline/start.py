
import config
from MusicSp import app
try:
    from pyrogram.enums import ButtonStyle
except ImportError:
    class ButtonStyle:
        PRIMARY = None
        SECONDARY = None
        SUCCESS = None
        DANGER = None
        DEFAULT = None
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true",
                style=ButtonStyle.PRIMARY,
            ),
            InlineKeyboardButton(
                text=_["S_B_2"], url=config.SUPPORT_GROUP,
                style=ButtonStyle.SUCCESS,
            ),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
                style=ButtonStyle.PRIMARY,
            
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper",
                              style=ButtonStyle.DANGER,
                              
                             )
        ],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID,
                                 style=ButtonStyle.PRIMARY,
                                ),
            
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_GROUP,
                                
                                 style=ButtonStyle.SUCCESS,
                                ),
        ],
        [
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL,
                                 style=ButtonStyle.PRIMARY,
                                ),
            InlineKeyboardButton(text="˹ 𝖲𝗈𝗎𝗋𝖼𝖾𝖢𝗈𝖽𝖾 ˼", url="https://github.com/DevloperSP/MusicSp",
                                  style=ButtonStyle.DANGER,
                                ),
        ],
    ]
    return buttons
