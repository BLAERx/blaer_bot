from aiogram import Bot, executor, Dispatcher, types
from tk import TOKEN_API
from filters import EmailCheck


bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot=bot)


@dp.message_handler(EmailCheck())
async def check_email(msg: types.Message) -> None:
    await msg.answer('Works!')

if __name__ == '__main__':
    executor.start_polling(dp)
    lol