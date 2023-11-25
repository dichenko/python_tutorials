from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = '5903893229:AAE-PYJD4CbQ7xATpH48jrGkQ40Lis'

# Создаем объекты бота и диспетчера
bot = Bot(BOT_TOKEN)
dp = Dispatcher()

# Cчетчик кликов
counter = 0

# Создаем кнопку клик
button_click = KeyboardButton(text='КЛИК!')

# Создаем игровую клавиатуру
keyboard = ReplyKeyboardMarkup(
    keyboard=[[button_click]],
    resize_keyboard=True)


@dp.message(F.text == '/start')
async def start_command(message: Message):
    await message.answer(
        'Это кликер. Кликай!', reply_markup=keyboard)


@dp.message(F.text == 'КЛИК!')
async def click(message: Message):
    global counter
    counter += 1
    await message.answer(f'Ты накликал {counter} раз')
    print(counter)



# Блок, который заставляет бота постоянно ходить на сервер телеграмма и спрашивать, есть ли новые сообщения
if __name__ == '__main__':
    dp.run_polling(bot)



