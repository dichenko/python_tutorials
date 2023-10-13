#Todo
# Приветствовать пользователя по имени. Имя хранится в сообщении (message.from_user.full_name)
# Добавить проверку, что ввели именно число
# Добавить проверку, чтобы не вводили слишком большие числа
# Добавить счетчик: сколько раз бот посчитал степень двойки


from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = '5903893229:AAE-PYy4CbQ79999485Akpj9GkQ40Lis'

# Создаем объекты бота и диспетчера
bot = Bot(BOT_TOKEN)
dp = Dispatcher()


# Когда пользователь нажал /start
@dp.message(F.text == '/start')
async def start_command(message: Message):
    await message.answer("Этот бот возводит двойку в любую степень.")
    await message.answer("Напиши любое целое число")


# Когда пользователь что-то ввел , возвращаем ему результат
@dp.message(F.text)
async def click(message: Message):
    text = message.text
    print(text)
    n = int(text)
    await message.answer(f"2 в степени {n} равно {(2**n)}")


# Блок, который заставляет бота постоянно ходить на сервер телеграмма и спрашивать, есть ли новые сообщения
if __name__ == '__main__':
    dp.run_polling(bot)


