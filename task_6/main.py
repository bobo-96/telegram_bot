from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


HELP_COMMAND = '''
<b>/start</b> -- <em>начало работы нашего бота</em>
<b>/help</b> -- <em>список существующих команд</em>
<b>/photo</b> -- <em>отправка фото</em>
'''

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id,
                           text = HELP_COMMAND,
                           parse_mode='HTML'
                           )
    await message.delete()

@dp.message_handler(commands=['photo'])
async def send_photo(message: types.Message):
    await bot.send_photo(chat_id = message.chat.id,
                           photo = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQeN_uxqqCN_Hi1UFgDWbq7a04pXTOmy1PODQ&usqp=CAU"
                           )
    await message.delete()

@dp.message_handler(commands=['location'])
async def send_point(message: types.Message):
    await bot.send_location(chat_id=message.from_user.id,
                            latitude=55,
                            longitude=74
                            )
    await message.delete()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
