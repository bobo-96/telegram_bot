from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API

# бот - сервер, который будет взаимодействовать с API telegram

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo_upper(message: types.Message):
    if message.text.count(' ') >= 1:
        await message.answer(text=message.text.upper())

if __name__ == '__main__':
    executor.start_polling(dp)