from keyboards.default.start_uchun import asosiy_keys
from aiogram import types
# from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.start_uchun import asosiy_keys
from loader import dp


@dp.message_handler(commands='start')
async def bot_start(message: types.Message):
    # await message.answer(f"Assalomu aleykum {message.from_user.full_name}!",reply_markup = asosiy_keys)
    await message.answer("🫵🏻 Siz kurslar nomli botga kirdingiz \
\nSiz bu bot orqali o'zingizga kerakli 👇🏻👇🏻 \
\nbo'lgan kursni topasiz degan umitdaman 👩🏻‍🎓🧑🏻‍🎓 \
\nQani boshladik 🙂😄",reply_markup=asosiy_keys)
