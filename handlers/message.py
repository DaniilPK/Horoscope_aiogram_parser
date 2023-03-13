import aiohttp
from aiogram import types, Bot
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent

from handlers.keyboard import Zodiaki


async def zadiaki(callbk: types.CallbackQuery,bot: Bot):
    await bot.send_chat_action(callbk.message.chat.id,'typing')
    BaseURL = f'https://orakul.com/horoscope/astrologic/general/{callbk.data}/today.html'
    HEADERS = {'User-Agent': UserAgent().random}

    async with aiohttp.ClientSession() as session:
        async with session.get(BaseURL, headers=HEADERS) as response:
            r = await aiohttp.StreamReader.read(response.content)
            soup = BS(r, 'html.parser')
            item = soup.find('p', {'class': ''})
            await callbk.message.delete()
            await callbk.message.answer(getattr(item, 'text','Попробуйте еще раз'),reply_markup=Zodiaki())
