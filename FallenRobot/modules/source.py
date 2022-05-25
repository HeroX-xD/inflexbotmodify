from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from FallenRobot import pbot as client


ANON = "https://telegra.ph/file/d3f447cac7ce533eff9ef.jpg"

@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=ANON,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [ɪɴғʟᴇx ʙᴏᴛ](t.me/inflex_bot)**

**» ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ :** [s ᴏ ᴍ ʏ ᴀ ᴊ ᴇ ᴇ ᴛ〘🇮🇳〙](tg://user?id=5124507794)
**» ᴩʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`
**» ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{o}` 
**» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{s}` 
**» ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{z}`

**ɪɴғʟᴇx ʙᴏᴛ sᴏᴜʀᴄᴇ ɪs ɴᴏᴡ x ᴀɴᴅ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ't ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ᴏᴡɴᴇʀ •", url="tg://user?id=5124507794"), 
                    InlineKeyboardButton(
                        "• sᴏᴜʀᴄᴇ •", url="https://t.me/herox_xd")
                ]
            ]
        )
    )

__mod_name__ = "Rᴇᴩᴏ"
