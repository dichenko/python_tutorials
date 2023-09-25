from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = '5903893229:AAE-PYJDsy4CbQ7xATpH48AkpjrGkQ40Lis'

# Создаем объекты бота и диспетчера
bot = Bot(BOT_TOKEN)
dp = Dispatcher()

# Словарь, в котором будут храниться данные пользователей
users = {}

# Создаем кнопки
button_click = KeyboardButton(text='КЛИК!')

# Создаем игровую клавиатуру
keyboard = ReplyKeyboardMarkup(
    keyboard=[[button_click]],
    resize_keyboard=True)


@dp.message(F.text == '/start')
async def start_command(message: Message):
    await message.answer(
        'Это кликер. Кликай!', reply_markup=keyboard)
    # Если пользователь только запустил бота и его нет в словаре
    # users - добавляем его в словарь
    if message.from_user.id not in users:
        users[message.from_user.id] = 0

    else:
        await message.answer(f'Ты накликал {users[message.from_user.id]} раз')


@dp.message(F.text == 'КЛИК!')
async def click(message: Message):
    users[message.from_user.id] += 1
    await message.answer(f'Ты накликал {users[message.from_user.id]} раз')
    print(users)


# Блок, который заставляет бота постоянно ходить на сервер телеграмма и спрашивать, есть ли новые сообщения
if __name__ == '__main__':
    dp.run_polling(bot)

#Todo
#Добавить кнопку СБРОС по которому у пользователя сбросится счетчик
#Добавить кнопку статистика, чтобы видеть, сколько игроков в боте
#Добавить количество кликов у лидера
#Добавить лидерборд: топ-3 игрока с лучшими результатами
#Сохранять данные игроков в файл, чтобы они не терялись после перезапуска
