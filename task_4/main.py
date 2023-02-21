from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Бот был успешно запущен')

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('<em>Привет <b>Добро пожаловать</b> в наш бот</em>', parse_mode='HTML')

@dp.message_handler(commands=['give'])
async def give_sticker(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEH0ttj80j9t3cTyWK8aFYk0rxAxdaT7AACOQADkP2aFRtRUoboZ1rBLgQ')
    await message.delete()


@dp.message_handler()
async def send_emoji(message: types.Message):
    await message.reply(message.text + '❤️')

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)