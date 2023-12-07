from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

detailed_information = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Режим работы библиотеки', callback_data='lom')],
    [InlineKeyboardButton(text='Планер на месяц', callback_data='planer')],
    [InlineKeyboardButton(text='Контактная информация', callback_data='contacts')],
    [InlineKeyboardButton(text='VK', url='https://vk.com/spb_cdb')]
])
