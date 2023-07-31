import asyncio
import logging
import requests
import json
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.filters import Command
from aiogram.types import Message, BotCommand, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup



# Токен вашего бота из BotFather
TOKEN = "59038___29:AAE-PYJDsy4CbQ7___pjrGkQ40Lis"

router = Router()

# Создаем кнопку
button_1: KeyboardButton = KeyboardButton(text='Где МКС?')

# Добавляем кнопку в клавиатуру
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=[[button_1]],
    resize_keyboard=True)


# Обрабатываем команду старт
@router.message(Command(commands=["start"]))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, <b>{message.from_user.full_name}!</b>",
                         reply_markup=keyboard)


# Обрабатываем команду "Где МКС?"
@router.message(F.text == "Где МКС?")
async def get_location(message: types.Message, bot: Bot):
    # Это адрес сайта, который следит за МКС
    api_url = 'http://api.open-notify.org/iss-now.json'

    # Запрашиваем координаты спутника
    response = requests.get(api_url)

    # Если ответ от сайта пришел
    if response.status_code == 200:
        # Переводим его в формат JSON
        d = json.loads(response.text)

        # Сохраняем координаты
        a, b = (d['iss_position']['longitude'], d['iss_position']['latitude'])

        # Генерируем ссылку на яндекс карты
        t = f"https://yandex.ru/maps/?ll={d['iss_position']['longitude']}%2C{d['iss_position']['latitude']}&z=4"

        # Создаем инлайн-кнопку со ссылкоц
        url_button_1: InlineKeyboardButton = InlineKeyboardButton(
            text='Открыть в Яндекс-картах',
            url=t)
        keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
            inline_keyboard=[[url_button_1]])

        # Отвечаем пользователю где МКС
        await message.answer(text=f"Координаты спутника: {a} {b}", reply_markup=keyboard)
    else:
        await message.answer(text="МКС потерялся =(")


# На все другие сообщения отвечаем "Не понял"
@router.message(F.text)
async def echo_handler(message: types.Message) -> None:
    try:
        await message.answer(text=f"Не понял", reply_markup=keyboard)
    except TypeError:
        await message.answer("Nice try!", reply_markup=keyboard)

# Задаем меню команд для бота
async def set_main_menu(bot: Bot):
    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(command='/start',
                   description='Начинаем!'),
        BotCommand(command='/help',
                   description='Справка по работе бота'),
        BotCommand(command='/support',
                   description='Поддержка'),
        BotCommand(command='/contacts',
                   description='Другие способы связи'),
        BotCommand(command='/payments',
                   description='Платежи')]

    await bot.set_my_commands(main_menu_commands)


async def main() -> None:
    dp = Dispatcher()
    dp.include_router(router)
    bot = Bot(TOKEN, parse_mode="HTML")
    
    # при старте бота задаем ему меню
    dp.startup.register(set_main_menu)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
