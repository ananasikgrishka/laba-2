from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Мне весело😁'), KeyboardButton(text='Мне грустно😢')]
], resize_keyboard=True)
