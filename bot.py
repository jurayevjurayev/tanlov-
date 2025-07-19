import asyncio
from aiogram import Bot, Dispatcher, types
import os

BOT_TOKEN = os.getenv("8068269788:AAFQwvSIK6Xp5UxYb1beKaeE7g7evrPWX8c")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
