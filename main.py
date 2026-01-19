from aiogram import Bot, Dispatcher, executor
import os

bot = Bot(token=os.getenv("8574328978:AAEsQda_kQAPXE3Eacb8lyNXcopdzJI2orc"))
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(msg):
    await msg.answer("Bot ishlayapti ✅")

executor.start_polling(dp)
