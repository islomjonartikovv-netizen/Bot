import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN topilmadi! Render Environment'ga BOT_TOKEN qo'ying.")

dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Bot ishlayapti ✅")

async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())