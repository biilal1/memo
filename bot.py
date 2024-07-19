from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from pyromod import listen



bot = Client(
    "mo",
    api_id=22284698,
    api_hash=80114fbfcdb5b886a9e69f31a7e6b248,
    bot_token=7327600929:AAHAwz7HCSfWnIbrzv_reoglpbxOAQeCAkY,
    plugins=dict(root="Maker")
    )

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    M_9_T = "M_9_T"
    await bot.send_message(M_9_T, "𓏺 𝘾َِ𝘳- 𝙉َِ𝘰َِ𝙐َِ𝘳 Ꮠ͋͢➢𝙀َِ𝘭َِ𝙃َِ𝘢َِ𝙆َِ𝘦َِ𝙈⤸")
    print("[INFO]: 𓏺 𝘾َِ𝘳- 𝙉َِ𝘰َِ𝙐َِ𝘳 Ꮠ͋͢➢𝙀َِ𝘭َِ𝙃َِ𝘢َِ𝙆َِ𝘦َِ𝙈⤸")
    await idle()
