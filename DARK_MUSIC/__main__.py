import requests
from pyrogram import Client as Bot

from DARK_MUSIC.config import API_HASH
from DARK_MUSIC.config import API_ID
from DARK_MUSIC.config import BG_IMAGE
from DARK_MUSIC.config import BOT_TOKEN
from DARK_MUSIC.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="DARK_MUSIC.modules"),
)

bot.start()
run()
