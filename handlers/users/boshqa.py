from loader import dp
from keyboards.default import start_uchun
from keyboards.inline import erkaklar_uchun
from aiogram.types import CallbackQuery,Message

@dp.callback_query_handler(text_contains="ing")
@dp.callback_query_handler(text_contains="mashq")
@dp.callback_query_handler(text_contains="tarix")
@dp.callback_query_handler(text_contains="kimyo")
@dp.callback_query_handler(text_contains="arif")
@dp.callback_query_handler(text_contains="bio")
@dp.callback_query_handler(text_contains="rus")
@dp.callback_query_handler(text_contains="arab")
@dp.callback_query_handler(text_contains="matem")
@dp.callback_query_handler(text_contains="grafika")
@dp.callback_query_handler(text_contains="savod")
@dp.callback_query_handler(text_contains="WEB_dasturF")
@dp.callback_query_handler(text_contains="madeling")
@dp.callback_query_handler(text_contains="WEB_dasturB")
@dp.callback_query_handler(text="salon")
@dp.callback_query_handler(text="chevar")
@dp.callback_query_handler(text="kulol")
@dp.callback_query_handler(text="usta")
@dp.callback_query_handler(text="duradgor")
@dp.callback_query_handler(text="kashta")
@dp.callback_query_handler(text="pishiriq")
@dp.callback_query_handler(text="bichish")
@dp.callback_query_handler(text="to'qish")
@dp.callback_query_handler(text="tikuv")
@dp.callback_query_handler(text="dizayner")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("O'zingizga kerakli tugmani bosing", reply_markup=erkaklar_uchun.barchasi_uchun)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="qaytishsh")
async def ayol_qaytish(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("O'zingizga kerakli tugmani bosing", reply_markup=start_uchun.ayol)
    await call.answer(cache_time=60)



@dp.callback_query_handler(text="qaytish")
async def ayol_qaytish(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("O'zingizga kerakli tugmani bosing", reply_markup=start_uchun.erkak)
    await call.answer(cache_time=60)





@dp.message_handler(text = "Orqaga ⬅️")
async def asosiy(ms:Message):
    await ms.answer("Bosh menu",reply_markup=start_uchun.asosiy_keys)
