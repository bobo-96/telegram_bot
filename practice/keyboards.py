from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

kb = ReplyKeyboardMarkup(resize_keyboard=True)
btn1 =KeyboardButton('/help')
btn2 =KeyboardButton('/description')
btn3 =KeyboardButton('/main')
btn6 = KeyboardButton('/photo')

kb2 = ReplyKeyboardMarkup(resize_keyboard=True)
btn3 =KeyboardButton('/main')
btn4 =KeyboardButton('/photo_1')
btn5 =KeyboardButton('/photo_2')


kb.add(btn1).insert(btn2).add(btn6)
kb2.add(btn4).insert(btn5).add(btn3)

ikb = InlineKeyboardMarkup(row_width=2)
ibtn1 = InlineKeyboardButton(text = '❤️',
                             callback_data='like'
                             )
ibtn2 = InlineKeyboardButton(text = '🖤',
                             callback_data='dislike'
                             )
ikb.add(ibtn1, ibtn2)
