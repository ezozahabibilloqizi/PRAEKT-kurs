from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from loader import dp 
from data.config import ADMINS
from states.yangi_state import Tanishish
# from keyboards.default.start_uchun import tugma

@dp.message_handler(text="Ro'yxatdan o'tish 📋")
async def register(ms:Message):
    await ms.answer("Ismingizni kiriting")
    await Tanishish.ism.set()

@dp.message_handler(state=Tanishish.ism)
async def ism_xona(ms:Message, state:FSMContext):
    ismbu = ms.text
    await state.update_data(name = ismbu)
    await ms.answer("Familiyangizni kiriting")
    await Tanishish.next()

@dp.message_handler(state=Tanishish.familiya)
async def familiya(ms:Message, state:FSMContext):
    familii = ms.text
    await state.update_data(last_name = familii)
    await ms.answer("Telefon raqamingizni kiriting")
    await Tanishish.next()

@dp.message_handler(state=Tanishish.tel_raqam)
async def raqam(ms:Message, state:FSMContext):
    raq = ms.text
    await state.update_data(number = raq)
    await ms.answer("Yashash joyingizni kiriting")
    await Tanishish.next()

@dp.message_handler(state=Tanishish.manzil)
async def manzili(ms:Message, state:FSMContext):
    man = ms.text
    await state.update_data(joy = man)
    data = await state.get_data()
    ismi = data.get("name")
    familia = data.get("last_name")
    tel_raqam = data.get("number")
    yashash = data.get("joy")
    await ms.answer(f"Qabul qilingan ma'lumotlar:\n✅ 'Ism' : {ismi}\n\
✅ 'Familiya' : {familia}\n✅ 'Telefon' : {tel_raqam}\n✅ 'manzil' : {yashash}")
    await dp.bot.send_message(chat_id=ADMINS[0],text = f"Foydalanuvchi kiritgan ma'lumotlar:\n✅ 'Ism' : {ismi}\n\
✅ 'Familiya' : {familia}\n✅ 'Telefon' : {tel_raqam}\n✅ 'manzil' : {yashash}")
    await state.finish()



