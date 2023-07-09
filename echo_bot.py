from aiogram import Bot, Dispatcher, executor, types
from tk import TOKEN_API

bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot=bot)


# @dp.message_handler(lambda msg: not msg.text.count(' '))
# async def handle_word(msg: types.Message) -> None:
#     await msg.answer('This sentence contains one word')
#
# @dp.message_handler(lambda msg: msg.text.count(' '))
# async def handle_rest(msg: types.Message) -> None:
#     await msg.answer('This sentence contains more than one word')
#
#
# @dp.message_handler(content_types='sticker')
# async def handle_sticker(msg: types.Message) -> None:
#     await msg.answer('This is sticker')
#
#
# @dp.message_handler(content_types='photo')
# async def handle_photo(msg: types.Message) -> None:
#     await msg.answer('This is photo')

# среднее арифметическое
# @dp.message_handler(commands=['start'])
# async def cmd_start(msg: types.Message) -> None:
#     await msg.answer('Write the numbers')
#
#
# @dp.message_handler(lambda msg: msg.text.repalce(' ', '').isdigit())
# async def handle_numbers(msg: types.Message) -> None:
#     arr = msg.text.split(' ')
#     await msg.answer(sum([int(num) for num in arr])/len(arr))


@dp.message_handler(commands=['help', 'start'])
async def cmd_start(msg: types.Message) -> None:
    await msg.answer('START || HELP')

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)
