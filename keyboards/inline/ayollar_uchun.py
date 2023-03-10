from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from keyboards.inline.calback_data import kampyuter_calback,dastur_calback,fan_calback,barcha_calback

ayollar_uchun = (InlineKeyboardMarkup( 
    inline_keyboard=[ 
        [
            InlineKeyboardButton(text="Kampyuter kurslari π»", callback_data="kampyuter")
        ],
        [ 
            InlineKeyboardButton(text="Pishiriqchilik π", callback_data="pishiriq")
        ],
        [ 
            InlineKeyboardButton(text="Dizaynerlik π", callback_data="dizayner")
        ],
        [ 
            InlineKeyboardButton(text="Bichuvchilik π§₯", callback_data="bichish")
        ],
        [ 
            InlineKeyboardButton(text="To'quvchilik π§Ά", callback_data="to'qish")
        ],
        [ 
            InlineKeyboardButton(text="Fan kurslari π", callback_data="fan")
        ],
        [ 
            InlineKeyboardButton(text="Tikuvchilik πͺ‘π§΅", callback_data="tikuv")
        ],
        [ 
            InlineKeyboardButton(text="Salonchilik ππ»",callback_data="salon")
        ],
        [ 
            InlineKeyboardButton(text="Kashtachilik πͺ’",callback_data="kashta")
        ],
        [ 
            InlineKeyboardButton(text="Orqaga β¬οΈ", callback_data="qaytishsh")
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
    "Arab_tili kursi π©π»βππ§π»βπ": "arab",
    "Rus_tili kursi ππ»ββοΈπ΅π»ββοΈ": "rus",
    "Ingliz_tili kursi πΆπ": "ing",
    "Mentalni arifmetika π":"arif",
    "Matematika kursi π’":"matem",
    "Biologiya kursi π©Ί":"bio",
    "Kimyo kursi π":"kimyo",
    "Ona tili va adabiyot kursi π©π»βπ«π§π»βπ«":"mashq",
    "Jahon va O'zbekiston tarixi kursi π":"tarix"
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


