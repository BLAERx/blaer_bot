import os
from PIL import ImageGrab
import secrets
from aiogram import Bot, Dispatcher, types, executor

from tk import TOKEN_API

bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def cmd_start(msg: types.Message) -> None:
    await msg.answer('Text')


@dp.message_handler(commands=['screen'])
async def cmd_screen(msg: types.Message) -> None:
    img = ImageGrab.grab()
    if not os.path.exists('static'):
        os.mkdir('static')
    os.chdir('static')
    img_name = secrets.token_hex(8) + '.png'
    img.save(img_name, format='PNG')

    await msg.answer_photo(photo=open(img_name, 'rb'))

if __name__ == '__main__':
    executor.start_polling(dp)
