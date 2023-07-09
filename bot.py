from aiogram import Bot, executor, Dispatcher, types

token = '6348121343:AAGMw-T3C7HBWG1NxLFivXvllgfK6Y4bAvo'

bot = Bot(token='6348121343:AAGMw-T3C7HBWG1NxLFivXvllgfK6Y4bAvo')
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['help', 'start'])
async def cmd_start(msg: types.Message):
    await msg.answer('Приветик')


@dp.message_handler()
async def send_echo(msg: types.Message):
    print(msg)
    await msg.answer(msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)
    lol