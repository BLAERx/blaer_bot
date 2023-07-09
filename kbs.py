from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_client = ReplyKeyboardMarkup()
b1 = KeyboardButton('Say 1')
b2 = KeyboardButton('Say 2', request_contact=True)
b3 = KeyboardButton('Say 3')

kb_client.add(b1).add(b2)
kb_client.row(b1, b2)
kb_client.add(b1).insert(b3)
