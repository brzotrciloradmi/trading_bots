import asyncio
import os
from telegram import Bot
from .telegram_bot_token import telegram_token, chat_id

BOT_TOKEN = telegram_token
CHAT_ID = chat_id

bot = Bot(token=BOT_TOKEN)

def notify(message):
    asyncio.run(bot.send_message(chat_id=int(CHAT_ID), text=message))

if __name__ == "__main__":
    asyncio.run(notify("Hello world."))
