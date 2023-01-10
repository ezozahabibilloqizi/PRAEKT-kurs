from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from keyboards.inline.calback_data import kampyuter_calback,dastur_calback,fan_calback,barcha_calback

erkakler_uchun = (InlineKeyboardMarkup( 
    inline_keyboard=[ 
        [
            InlineKeyboardButton(text="Kampyuter kurslari 💻", callback_data="kampyuter")
        ],
        [ 
            InlineKeyboardButton(text="Duradgorlik 🚪", callback_data="duradgor")
        ],
        [ 
            InlineKeyboardButton(text="Ustachilik 🏠", callback_data="usta")
        ],
        [ 
            InlineKeyboardButton(text="Fan kurslari 📕", callback_data="fan")
        ],
        [ 
            InlineKeyboardButton(text="kulolchilik 🍶", callback_data="kulol")
        ],
        [ 
            InlineKeyboardButton(text="Chevarchilik 🪡🧵", callback_data="chevar")
        ],
        [ 
            InlineKeyboardButton(text="Orqaga ⬅️", callback_data="qaytish")
        ]
    ]
))



kampyuter = InlineKeyboardMarkup(row_width=1)

savod = InlineKeyboardButton(text="Kampyuter savodxonligi 💻", 
	callback_data=kampyuter_calback.new(item_name="savod"))
kampyuter.insert(savod)

dastur = InlineKeyboardButton(text="🌐 Dasturlash", 
	callback_data=kampyuter_calback.new(item_name="dastur"))
kampyuter.insert(dastur)


back_button = InlineKeyboardButton(text="🔙 Kurslar ro'yxatiga o'tish", callback_data="cancel")
kampyuter.insert(back_button)





# 3 - usul
dasturlash = {
    "WEB dasturlashning Backend yo'nalishi 🐍": "WEB_dasturB",
    "WEB dasturlashning FrontEnd yo'nalishi 📊": "WEB_dasturF",
    "Grafik dizayn yo'nalishi 🔺🔻": "grafika",
    "3D madeling yo'nalishi 🔲":"madeling"
}

dastur_menu = InlineKeyboardMarkup(row_width=1)
for key, value in dasturlash.items():
    dastur_menu.insert(InlineKeyboardButton(text=key, 
    	callback_data=dastur_calback.new(item_name=value)))
dastur_menu.insert(back_button)



fan_kurs = {
    "Arab_tili kursi": "arab",
    "Rus_tili kursi": "rus",
    "Ingliz_tili kursi": "ing",
    "Mentalni arifmetika":"arif",
    "Matematika kursi":"matem",
    "Biologiya kursi":"bio",
    "Kimyo kursi":"kimyo",
    "Ona tili va adabiyot kursi":"mashq",
    "Jahon va O'zbekiston tarixi kursi":"tarix"
}
fan_menu = InlineKeyboardMarkup(row_width=1)
for key, value in fan_kurs.items():
    fan_menu.insert(InlineKeyboardButton(text=key, 
    	callback_data=fan_calback.new(item_name=value)))
fan_menu.insert(back_button)




barcha = { 
    "Joylashuvlarimmiz 📍":"joy",
    "Yutuqlarimmiz 🏆":"yutuq",
    "Maqsadimmiz 📑":"maqsad",
    "Bizning telegram kanalimmiz 📱":"telegram",
    "Bizning You tube kanalimmiz 🌐":"you_tube"
}
barchasi_uchun = InlineKeyboardMarkup(row_width=1)
for key, value in barcha.items():
    barchasi_uchun.insert(InlineKeyboardButton(text=key, 
    	callback_data=barcha_calback.new(item_name=value)))
barchasi_uchun.insert(back_button)


