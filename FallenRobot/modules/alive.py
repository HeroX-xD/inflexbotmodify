import os
import re
import random
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from FallenRobot.events import register
from FallenRobot import telethn as tbot


PHOTO = [
    "https://telegra.ph/file/1b8fe6c2e2a60102922ff.jpg",
    "https://telegra.ph/file/d3f447cac7ce533eff9ef.jpg",
]

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ 𝗜𝗻𝗳𝗹𝗲𝘅 𝗕𝗼𝘁 🇮🇳​**\n━━━━━━━━━━━━━━━━━━━\n\n"
  TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [s ᴏ ᴍ ʏ ᴀ ᴊ ᴇ ᴇ ᴛ〘🇮🇳〙](https://t.me/herox_xd)** \n\n"
  TEXT += f"» **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
  TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
  TEXT += f"» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n━━━━━━━━━━━━━━━━━\n\n"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", "https://t.me/inflex_robot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/AmTrickyAbhii")]]
  ran = random.choice(PHOTO)
  await tbot.send_file(event.chat_id, ran, caption=TEXT,  buttons=BUTTON)

## Alive mod
