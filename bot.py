from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from pyromod import listen



bot = Client(
    "mo",
    api_id="22284698",
    api_hash="80114fbfcdb5b886a9e69f31a7e6b248",
    bot_token="7327600929:AAF3E7EXyjnlmRlzBUvTu3NSWZcwEo66uC0",
    plugins=dict(root="Maker")
    )

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    M_9_T = "M_9_T"
    await bot.send_message(M_9_T, "**تم تشغيل ال صانع بنجاح عزيزي المطور ...🥀،**")
    print("[INFO]: تم تشغيل الصانع وارسال رسالة للمطور⚡🚦.")
    await idle()
