import asyncio
import logging
import requests
import json

from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup)

TOKEN = "_____"


router = Router()

button_1: KeyboardButton = KeyboardButton(text='Где МКС?')
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_1]])


@router.message(Command(commands=["start"]))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, <b>{message.from_user.full_name}!</b>",
                         reply_markup=keyboard,
                         resize_keyboard=True)


@router.message(F.text == "Где МКС?")
async def get_location(message: types.Message, bot:Bot):
    api_url = 'http://api.open-notify.org/iss-now.json'
    response = requests.get(api_url)
    if response.status_code == 200:
        d = json.loads(response.text)
        await message.answer(text=f"https://yandex.ru/maps/?ll={d['iss_position']['longitude']}%2C{d['iss_position']['latitude']}&z=4")
    else:
        await message.answer(text="МКС потерялся =(")


@router.message()
async def echo_handler(message: types.Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    dp = Dispatcher()
    dp.include_router(router)
    bot = Bot(TOKEN, parse_mode="HTML")
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
