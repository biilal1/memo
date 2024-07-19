from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from pyromod import listen



bot = Client(
    "mo",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Maker")
    )

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    M_9_T = "M_9_T"
    await bot.send_message(M_9_T, "𓏺 𝘾َِ𝘳- 𝙉َِ𝘰َِ𝙐َِ𝘳 Ꮠ͋͢➢𝙀َِ𝘭َِ𝙃َِ𝘢َِ𝙆َِ𝘦َِ𝙈⤸")
    print("[INFO]: 𓏺 𝘾َِ𝘳- 𝙉َِ𝘰َِ𝙐َِ𝘳 Ꮠ͋͢➢𝙀َِ𝘭َِ𝙃َِ𝘢َِ𝙆َِ𝘦َِ𝙈⤸")
    await idle()
