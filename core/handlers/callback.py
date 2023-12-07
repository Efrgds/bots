from aiogram import Bot, types
from aiogram.enums import ParseMode
from aiogram.types import FSInputFile


async def detailed_information(call: types.CallbackQuery, bot: Bot):
    code = call.data
    if code == 'lom':
        photo = FSInputFile(r'C:\Users\User\PycharmProjects\123\bot\photo\lom.jpg')
        await call.message.answer_photo(photo)
    elif code == 'contacts':
        await call.answer(
            text=f'     <b>Наши телефоны:</b>\n\n'
                 f'516-25-09 Заведующий\n'
                 f'599-99-49 Методист\n'
                 f'598-82-35 Отдел краеведения\n'
                 f'599-98-77 Младший и старший абонементы',
            show_alert=True, parse_mode=ParseMode.HTML)
    elif code == 'planer':
        photo = FSInputFile(r'C:\Users\User\PycharmProjects\123\bot\photo\nvmbr.jpg')
        await call.message.answer_photo(photo, caption='')
