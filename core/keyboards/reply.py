from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Продлить книгу'),
     KeyboardButton(text='Уточнить наличие книги'),
     KeyboardButton(text='Популярные видео')],
    [KeyboardButton(text='Подробная информация'),
     KeyboardButton(text='Задать вопрос')]
], resize_keyboard=True, one_time_keyboard=False, input_field_placeholder='Выбери кнопку ↓')
