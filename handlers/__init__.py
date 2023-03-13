from aiogram import Router, F
from aiogram.filters import CommandStart

from handlers.message import zadiaki
from handlers.start import start


def register_router(router: Router):
    router.message.filter(F.chat.type == 'private')
    router.message.register(start, CommandStart())
    router.callback_query.register(zadiaki, F.data == 'aries')
    router.callback_query.register(zadiaki, F.data == 'taurus')
    router.callback_query.register(zadiaki, F.data == 'gemini')
    router.callback_query.register(zadiaki, F.data == 'cancer')

    router.callback_query.register(zadiaki, F.data == 'lion')
    router.callback_query.register(zadiaki, F.data == 'virgo')
    router.callback_query.register(zadiaki, F.data == 'libra')
    router.callback_query.register(zadiaki, F.data == 'scorpio')

    router.callback_query.register(zadiaki, F.data == 'sagittarius')
    router.callback_query.register(zadiaki, F.data == 'capricorn')
    router.callback_query.register(zadiaki, F.data == 'aquarius')
    router.callback_query.register(zadiaki, F.data == 'pisces')
