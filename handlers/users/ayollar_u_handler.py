from aiogram.types import Message
from loader import dp
from keyboards.inline import ayollar_uchun
from keyboards.default import start_uchun
from aiogram.types import Message, CallbackQuery

@dp.message_handler(text = "Ayollar uchun 👩🏻‍🎓")
async def asosiy(ms:Message):
    await ms.answer("O'zingizga kerakli tugmani bosing",reply_markup=start_uchun.ayol)

@dp.message_handler(text_contains = "Ayollar uchun kurslar 📚")
async def erkak(ms:Message):
    await ms.answer("Bu ayollar uchun kurslar ro'yxati siz o'zingizga kerakligini tanlang",reply_markup=ayollar_uchun.ayollar_uchun)

@dp.callback_query_handler(text="kampyuter")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("O'zingizga kerakli tugmani bosing", reply_markup=ayollar_uchun.kampyuter)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=ayollar_uchun.ayollar_uchun)
    await call.answer()

@dp.callback_query_handler(text_contains="dastur")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("O'zingizga kerakli tugmani bosing", reply_markup=ayollar_uchun.dastur_menu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="fan")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("O'zingizga kerakli tugmani bosing", reply_markup=ayollar_uchun.fan_menu)
    await call.answer(cache_time=60)
