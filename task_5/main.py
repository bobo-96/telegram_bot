from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API

HELP_COMMAND = '''
<b>/help</b> - <em>спислк комманд</em>
<b>/give</b> = <em>отправляет котика</em>
'''
bot = Bot(TOKEN_API)

dp = Dispatcher(bot)

async def on_startup(_):
    print("Я запустился")

@dp.message_handler(content_types=['sticker'])
async def sticker_id(message: types.Message):
    await message.answer(message.sticker.file_id)


@dp.message_handler(commands=['give'])
async def send_cat_emoji(message: types.Message):
    await message.answer("Смотри какой красивый котик")
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEH1cFj9GILtbJGd3NI6rQCXyUE93JhKQACLQADkP2aFQOk0QHS--S5LgQ')


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(HELP_COMMAND, parse_mode='HTML')


@dp.message_handler()
async def send_hurt(message: types.Message):
    if '❤️' in message.text:
        await message.answer('🖤')
    elif '✅' in message.text:
        a = message.text.count('✅')
        await message.answer('✅' * a)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)