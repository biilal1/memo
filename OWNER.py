import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

OWNER = ["BDB0B"]
OWNER_NAME = "𓏺 𝘾َِ𝘳- 𝙉َِ𝘰َِ𝙐َِ𝘳 Ꮠ͋͢➢𝙀َِ𝘭َِ𝙃َِ𝘢َِ𝙆َِ𝘦َِ𝙈⤸"
BOT_TOKEN = getenv("7324813477:AAEU31qskRcD8U-M4IsGpLeGnTT8UIhQRR4")
DATABASE = getenv("mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
CHANNEL = "https://t.me/sourceav"
GROUP = "https://t.me/va_source"
VID_SO = "https://telegra.ph/file/4fda78aaf200bf313be62.jpg"
PHOTO = "https://telegra.ph/file/4fda78aaf200bf313be62.jpg"
LOGS = "M_9_T"
