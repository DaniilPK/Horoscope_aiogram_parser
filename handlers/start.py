from aiogram import types
from handlers.keyboard import Zodiaki


async def start(message: types.Message):
    await message.answer('Приветствую это бот гороскоп.\n'
                         'Выберите свой знак зодиака что бы узнать предсказание нас сегодня',reply_markup=Zodiaki())