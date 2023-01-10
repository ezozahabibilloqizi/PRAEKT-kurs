from aiogram.types import Message
from loader import dp
from keyboards.inline import erkaklar_uchun
# from keyboards.inline.calback_data import kampyuter_calback
from keyboards.default import start_uchun
from aiogram.types import Message, CallbackQuery


@dp.message_handler(text = "Erkaklar uchun 🧑🏻‍🎓")
async def asosiy(ms:Message):
    await ms.answer("O'zingizga kerakli tugmani bosing",reply_markup=start_uchun.erkak)

@dp.message_handler(text_contains = "Erkaklar uchun kurslar 📚")
async def erkak(ms:Message):
    await ms.answer("Bu erkaklar uchun kurslar ro'yxati siz o'zingizga kerakligini tanlang",reply_markup=erkaklar_uchun.erkakler_uchun)

@dp.callback_query_handler(text="kampyuter")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("O'zingizga kerakli tugmani bosing", reply_markup=erkaklar_uchun.kampyuter)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=erkaklar_uchun.erkakler_uchun)
    await call.answer()

@dp.callback_query_handler(text_contains="dastur")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("O'zingizga kerakli tugmani bosing", reply_markup=erkaklar_uchun.dastur_menu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="fan")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("O'zingizga kerakli tugmani bosing", reply_markup=erkaklar_uchun.fan_menu)
    await call.answer(cache_time=60)
