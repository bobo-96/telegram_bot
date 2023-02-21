from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)



if __name__ == '__main__':
    executor.start_polling(dp)