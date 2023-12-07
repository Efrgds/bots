import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage

from core.handlers import callback, send_media, basic
# process_question_command, process_answer_command
from core.utils.db import Database
from core.keyboards import reply
from core.settings import settings

HELP_COMMAND = """
/helo - список команд
/start - работа с ботом 
"""
logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()
bot = Bot(token="6628132120:AAGDYcUIRo2EAHMSILIA0KALrtvGvIFoEHw", parse_mode='HTML')
db = Database
dp = Dispatcher()


async def start_bot(bot: Bot):
    # await db.create_connection()
    await bot.send_message(settings.bots.admin_id, text='Запущен')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Остановлен')


async def help(message: types.Message):
    await message.reply('text=HELP_COMMAND')


async def start(message: types.Message):
    # await db_start()
    # await create_users(user_id=message.from_user.id)
    # await edit_users(state, user_id=message.from_user.id)
    await message.answer('Добро пожаловать в наш бот!', reply_markup=reply.reply_keyboard)


dp.startup.register(start_bot)
dp.message.register(basic.get_inline, F.text == 'Подробная информация')
dp.message.register(basic.get_extend, F.text == 'Продлить книгу')
# dp.message.register(basic.forward_message, F.text)
dp.message.register(send_media.get_media_group, F.text == 'Популярные видео')
dp.message.register(send_media.get_photo, F.text == 'Режим работы библиотеки')
dp.callback_query.register(callback.detailed_information, F.data.startswith('plan'))
dp.callback_query.register(callback.detailed_information, F.data.startswith('lo'))
# dp.callback_query.register(callback.detailed_information, F.data.startswith('cont'))
# dp.message.register(process_question_command, Command('questions'))
# dp.message.register(process_answer_command, Command('answer'))
# dp.message.register(process_answer, F.text == 'Задать вопрос')

dp.message.register(start)
dp.shutdown.register(stop_bot)

if __name__ == "__main__":
    try:
        asyncio.run(dp.start_polling(bot))

    finally:
        asyncio.run(bot.session.close())
