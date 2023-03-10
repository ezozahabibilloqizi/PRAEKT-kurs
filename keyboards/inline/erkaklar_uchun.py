from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from keyboards.inline.calback_data import kampyuter_calback,dastur_calback,fan_calback,barcha_calback

erkakler_uchun = (InlineKeyboardMarkup( 
    inline_keyboard=[ 
        [
            InlineKeyboardButton(text="Kampyuter kurslari π»", callback_data="kampyuter")
        ],
        [ 
            InlineKeyboardButton(text="Duradgorlik πͺ", callback_data="duradgor")
        ],
        [ 
            InlineKeyboardButton(text="Ustachilik π ", callback_data="usta")
        ],
        [ 
            InlineKeyboardButton(text="Fan kurslari π", callback_data="fan")
        ],
        [ 
            InlineKeyboardButton(text="kulolchilik πΆ", callback_data="kulol")
        ],
        [ 
            InlineKeyboardButton(text="Chevarchilik πͺ‘π§΅", callback_data="chevar")
        ],
        [ 
            InlineKeyboardButton(text="Orqaga β¬οΈ", callback_data="qaytish")
        ]
    ]
))



kampyuter = InlineKeyboardMarkup(row_width=1)

savod = InlineKeyboardButton(text="Kampyuter savodxonligi π»", 
	callback_data=kampyuter_calback.new(item_name="savod"))
kampyuter.insert(savod)

dastur = InlineKeyboardButton(text="π Dasturlash", 
	callback_data=kampyuter_calback.new(item_name="dastur"))
kampyuter.insert(dastur)


back_button = InlineKeyboardButton(text="π Kurslar ro'yxatiga o'tish", callback_data="cancel")
kampyuter.insert(back_button)





# 3 - usul
dasturlash = {
    "WEB dasturlashning Backend yo'nalishi π": "WEB_dasturB",
    "WEB dasturlashning FrontEnd yo'nalishi π": "WEB_dasturF",
    "Grafik dizayn yo'nalishi πΊπ»": "grafika",
    "3D madeling yo'nalishi π²":"madeling"
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
    "Joylashuvlarimmiz π":"joy",
    "Yutuqlarimmiz π":"yutuq",
    "Maqsadimmiz π":"maqsad",
    "Bizning telegram kanalimmiz π±":"telegram",
    "Bizning You tube kanalimmiz π":"you_tube"
}
barchasi_uchun = InlineKeyboardMarkup(row_width=1)
for key, value in barcha.items():
    barchasi_uchun.insert(InlineKeyboardButton(text=key, 
    	callback_data=barcha_calback.new(item_name=value)))
barchasi_uchun.insert(back_button)


