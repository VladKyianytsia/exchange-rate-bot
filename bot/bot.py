import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import FSInputFile
from dotenv import load_dotenv

from db.actions import generate_exchange_rates_xlsx

load_dotenv()


bot = Bot(token=os.getenv("BOT_TOKEN"))

dp = Dispatcher()


@dp.message(Command("get_exchange_rate"))
async def cmd_start(message: types.Message):
    file_path = generate_exchange_rates_xlsx()
    xlsx_file = FSInputFile(file_path)
    await message.answer_document(xlsx_file)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
