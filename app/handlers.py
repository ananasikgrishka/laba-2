from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
import app.keyboards as kb
import photos
from random import randint

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет! Тут ну очень смешные картинки', reply_markup=kb.main)


@router.message(F.text == 'Мне весело😁')
async def fun(message: Message):
    await message.answer_photo(photo=f'{photos.fun[randint(0, len(photos.fun) - 1)]}')


@router.message(F.text == 'Мне грустно😢')
async def sad(message: Message):
    await message.answer_photo(photo=f'{photos.sad[randint(0, len(photos.sad) - 1)]}')





