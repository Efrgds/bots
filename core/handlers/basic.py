import json

from aiogram import types, Bot
from aiogram.client import bot
from core.keyboards.inline import detailed_information

# from core.middlewares.fsm import Answer
# from core.utils.db import get_unanswered_questions
# from main import db

chat_id = '-4005007343'


async def get_inline(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}. 123',
                         reply_markup=detailed_information)


async def get_extend(message: types.Message):
    await message.reply(f'Введите номер читательского билета')
    json_str = json.dumps(message.dict(), default=str)
    print(json_str)


# async def process_question_command(message: types.Message, bot: Bot):
#     if len(message.text) > 10:
#         question = message.text.split('/question')[-1]
#         await db.add_question(message.from_user.id, message.text)
#         await bot.send_message(chat_id='', text=f"✉ Новое уведомление! {message.from_user.first_name}:{question}")
#
#     else:
#         await message.answer(f"Сообщение ne отправлено!")

#
# async def process_answer_command(message: types.Message, state: FSMContext):
#     questions = await get_unanswered_questions()
#     if len(questions) > 0:
#         question = questions[0]
#         await message.answer(f"poluchi {question[1]}:\n\n{question[2]}")
#         await Answer.waiting_for_answer.set()
#         await state.update_data(question_id=question[0], admin_id=question[1])
#     else:
#         await message.answer('no q an')

#
# async def process_answer(message: types.Message, state: FSMContext):
#     data = await state.get_data()
#     question_id = data.get('question_id')
#     user_id = data.get('user_id')
#     await db.update_questions_id(question_id, message.text)
#     await message.reply('sdfgjkl')
#     await bot.send_message(chat_id=user_id, text=f"\nОтвет от тех.поддержки:\n\n`{message.text}`")
#     await state.finish
