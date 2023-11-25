# Todo
# Создать клавиатуры
# Дописать игровую логику
# Сделать справку
# Сделать обработку некорректных сообщений
# Обработать "Не хочу"
# Сделать статистику игр (Всего, выиграл, проиграл, ничья, в процентах)

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

import random
from dotenv import load_dotenv  # Библиотека python-dotenv
import os

# Предварительно создать файл .env и запистаь туда свой BOT_TOKEN
load_dotenv()

# Теперь клавиатуры будут жить в отдельном файле
from keyboards import yes_no_keyboard, game_kb

# Создаем объекты бота и диспетчера
bot = Bot(os.getenv('BOT_TOKEN'))
dp = Dispatcher()


@dp.message(F.text == '/start')
async def start_command(message: Message):
    await message.answer(
        'Это игра КНБ. Играем?', reply_markup=yes_no_keyboard)


@dp.message(F.text == 'Давай!')
async def game(message: Message):
    await message.answer(
        'Твой ход!', reply_markup=game_kb)


@dp.message(F.text.in_(["Камень 🗿", 'Ножницы ✂', 'Бумага 📜']))
async def game(message: Message):
    mas = ["Камень 🗿", 'Ножницы ✂️', 'Бумага 📜']
    bot_choise = random.choice(mas)
    print(message.text)
    await message.answer(f'Ты загадал {message.text}, а я загадал {bot_choise}')
    await message.answer(f'Я пока не знаю, кто выиграл. Мой програмист меня не доделал, прости.')
    await message.answer(f'Хочешь еще раз сыграть?',
                         reply_markup=yes_no_keyboard)


@dp.message()
async def default(message: Message):
    print(message.text)



if __name__ == '__main__':
    dp.run_polling(bot)


