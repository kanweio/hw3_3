from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton('Да'), KeyboardButton('Нет'))

cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton('CANCEL'))

