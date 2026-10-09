import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    MenuButtonWebApp,
    Message,
    WebAppInfo,
)
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.environ["BOT_TOKEN"]
WEBAPP_URL = os.environ["WEBAPP_URL"]  # HTTPS-адрес webapp/index.html

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message) -> None:
    kb = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="💱 Курс валют", web_app=WebAppInfo(url=WEBAPP_URL))]]
    )
    await message.answer("Открой приложение, чтобы увидеть курс валют и сегодняшнюю дату:", reply_markup=kb)


async def main() -> None:
    bot = Bot(BOT_TOKEN)
    # Кнопка «Курс» слева от поля ввода — открывает мини-апп без /start
    await bot.set_chat_menu_button(menu_button=MenuButtonWebApp(text="Курс", web_app=WebAppInfo(url=WEBAPP_URL)))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
