from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_toprost = KeyboardButton("ТОП +")
button_toppaden = KeyboardButton("ТОП -")
button_world = KeyboardButton("Индексы и сырье")

greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_toprost, button_toppaden).row(button_world)




