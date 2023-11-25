from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Создаем кнопки с ответами согласия и отказа
button_yes = KeyboardButton(text="Давай!")
button_no = KeyboardButton(text="Не охота =(")

# Создаем клавиатуру да-нет
yes_no_keyboard = ReplyKeyboardMarkup(
    keyboard= [[button_yes],[button_no]],
    resize_keyboard=True,
    one_time_keyboard=True)


# Создаем кнопки игровой клавиатуры
button_1 = KeyboardButton(text="Камень 🗿")
button_2 = KeyboardButton(text="Ножницы ✂")
button_3 = KeyboardButton(text="Бумага 📜")

# Создаем игровую клавиатуру
game_kb = ReplyKeyboardMarkup(
    keyboard=[[button_1],
              [button_2],
              [button_3]],
    resize_keyboard=True,
    one_time_keyboard=True
)


