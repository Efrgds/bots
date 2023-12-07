from aiogram import Bot
from aiogram.types import Message, FSInputFile, InputMediaVideo


async def get_media_group(message: Message, bot: Bot):
    video1_mg = InputMediaVideo(type='video',
                                media=FSInputFile(r'C:\Users\User\PycharmProjects\123\video\IMG_8559.MOV'),
                                caption='123')
    video2_mg = InputMediaVideo(type='video',
                                media=FSInputFile(r'C:\Users\User\PycharmProjects\123\video\IMG_8490.MOV'),
                                caption='123')
    video3_mg = InputMediaVideo(type='video',
                                media=FSInputFile(r'C:\Users\User\PycharmProjects\123\video\IMG_8526.MOV'),
                                caption='123')
    media = [video1_mg, video2_mg, video3_mg]
    await bot.send_media_group(message.chat.id, media)


async def get_photo(message: Message, bot: Bot):
    photo = FSInputFile(r'C:\Users\User\PycharmProjects\123\bot\photo\lom.jpg')
    await bot.send_photo(message.chat.id, photo, caption='its photo')

# async def (call: types.CallbackQuery):
#     if call.data == 'lo':
#         photo = FSInputFile(r'C:\Users\User\PycharmProjects\123\bot\photo\nvmbr.jpg')
#     await call.message.answer_photo(photo, caption='its photo')
