from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

asosiy_keys = ReplyKeyboardMarkup( 
    keyboard=[
        [
            KeyboardButton("Erkaklar uchun 🧑🏻‍🎓"),
            KeyboardButton("Ayollar uchun 👩🏻‍🎓")
        ],
        [ 
            KeyboardButton("Ro'yxatdan o'tish 📋")
        ]
    ],
    resize_keyboard=True,one_time_keyboard=True
)

erkak = ReplyKeyboardMarkup( 
    keyboard=[ 
        [ 
            KeyboardButton("Erkaklar uchun kurslar 📚"),
            KeyboardButton("Biz haqimizda 📋")
        ],
        [ 
            KeyboardButton("Orqaga ⬅️")
        ]
    ],
    resize_keyboard=True,one_time_keyboard=True
)

ayol = ReplyKeyboardMarkup( 
    keyboard=[ 
        [ 
            KeyboardButton("Ayollar uchun kurslar 📚"),
            KeyboardButton("Biz haqimizda 📋")
        ],
            [ 
            KeyboardButton("Orqaga ⬅️")
        ]
    ],
    resize_keyboard=True,one_time_keyboard=True
)

