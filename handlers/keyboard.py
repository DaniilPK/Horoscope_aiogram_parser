from aiogram import types


def Zodiaki():
    buttons = [
        [
            types.InlineKeyboardButton(text="Овен", callback_data="aries"),
            types.InlineKeyboardButton(text="Телец", callback_data="taurus"),
            types.InlineKeyboardButton(text="Близнецы", callback_data="gemini"),
            types.InlineKeyboardButton(text="Рак", callback_data="cancer"),
        ],

        [
            types.InlineKeyboardButton(text="Лев", callback_data="lion"),
            types.InlineKeyboardButton(text="Дева", callback_data="virgo"),
            types.InlineKeyboardButton(text="Весы", callback_data="libra"),
            types.InlineKeyboardButton(text="Скорпион", callback_data="scorpio"),
        ],
        [
            types.InlineKeyboardButton(text="Стрелец", callback_data="sagittarius"),
            types.InlineKeyboardButton(text="Козерог", callback_data="capricorn"),
            types.InlineKeyboardButton(text="Водолей", callback_data="aquarius"),
            types.InlineKeyboardButton(text="Рыбы", callback_data="pisces"),
        ],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
