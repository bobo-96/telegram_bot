from aiogram import Bot, Dispatcher, executor, types
from keyboards import kb, kb2, ikb
from config import TOKEN_API

HELP_COMMANDS = '''
<b>/help</b> --- <em>все доступные команды</em>
<b>/start</b> --- <em>запуск бота</em>
<b>/description</b> --- <em>описание бота</em>
<b>/main</b> --- <em>возврат в главное меню</em>
<b>/photo</b> --- <em>голосование за лучшее фото</em>
'''


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Я запустился Ехууууаааа')

@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Добро пожаловать в наш бот /n всю подробрную информацию можете найти по команде /help',
                           reply_markup=kb
                           )
    await message.delete()
    
@dp.message_handler(commands=['help'])
async def help(message:types.Message):
    await bot.send_message(message.from_user.id,
                        HELP_COMMANDS,
                        parse_mode='HTML')
    await message.delete()
    
@dp.message_handler(commands=['description'])
async def description(message:types.Message):
    await message.answer(text='Бот создан для тестирования изученных технологий')
    await message.delete()

@dp.message_handler(commands=['main'])
async def main(message:types.Message):
    await message.reply(text='back',
                        reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=['photo'])
async def photo(message:types.Message):
    await bot.send_message(chat_id=message.chat.id,
                        text='Добро пожаловать в голосование за лучшее фото выбирете в меню фото',
                        reply_markup=kb2)
    await message.delete()

@dp.message_handler(commands=['photo_1'])
async def photo_1(message:types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         caption='Котик намбр ван',
                         photo='https://i.pinimg.com/736x/ba/92/7f/ba927ff34cd961ce2c184d47e8ead9f6.jpg',
                         reply_markup=ikb
                        )
    await message.delete()

@dp.message_handler(commands=['photo_2'])
async def photo_2(message:types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         caption='Котик намбр дван',
                         photo='https://i.ytimg.com/vi/0xqkksHov58/maxresdefault.jpg',
                         reply_markup=ikb
                        )
    await message.delete()

@dp.callback_query_handler()
async def vote_callback(callback: types.CallbackQuery):
    if callback.data == 'like':
        await callback.answer(text='Тебе понравился котик')
    await callback.answer(text='Тебе не понравился котик')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)