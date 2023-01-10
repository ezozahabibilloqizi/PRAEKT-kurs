from aiogram.dispatcher.filters.state import State,StatesGroup


class Tanishish(StatesGroup):
    ism = State()
    familiya = State()
    tel_raqam = State()
    manzil = State()