from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API
import string
import random

DESCRIPTION = '''
Этот бот создан для изучения телеграм ботов
'''
numbers_of_count = 0

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await message.answer(text=DESCRIPTION)

@dp.message_handler(commands=['count'])
async def count(message: types.Message):
    global numbers_of_count
    await message.reply(numbers_of_count)
    numbers_of_count += 1

@dp.message_handler()
async def check_zero(message: types.Message):
    if '0' in message.text:
        return await message.reply('Yes')
    await message.reply('No')

@dp.message_handler()
async def random_answer(message: types.Message):
    await message.reply(text = random.choice(string.ascii_letters))




if __name__ == '__main__':
    executor.start_polling(dp)