from aiogram.types import Message
from loader import dp, bot
from aiogram.dispatcher import filters
import random
import time
from Keyboard import create_kb_mult100, create_nex_mult_pos100
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
import settings
from Keyboard.callback import callback
from DataBase import update_user_answer,update_bot_answer,check_user_answer



@dp.callback_query_handler(callback.filter(btn='next_mult100'))
@dp.callback_query_handler(callback.filter(menu='mult_up100'))
async def multipl(message: Message | CallbackQuery):
    user = message.from_user.id
    message_id = message.message.message_id
    chat_id = message.message.chat.id
    a = random.randint(1, 1000)
    b = random.randint(1, 100)
    result = a * b
    update_bot_answer(result,user)                           # кладем в бд верный ответ

    # await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
    #                                 text=f'{a} * {b} = ?', reply_markup=create_kb_mult(settings.ENTER))
    await bot.edit_message_media(media=InputMediaPhoto(media=settings.PICTURE, caption=f'{a} * {b} = ?'),
                                 chat_id=chat_id,
                                 message_id=message_id, reply_markup=create_kb_mult100(settings.ENTER))

@dp.callback_query_handler(callback.filter(menu='main_mult100'))
async def enter(call: CallbackQuery):
    user = call.from_user.id
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    res = str(check_user_answer(user)[0])                    # из бд берем текущий результат
    _, _, num = call.data.split(':')
    if num.isdigit():
        res += num                                           # и конкатинируем
    else:
        if len(res)==1:
            res = 0
        else:
            res = res[:-1]
    update_user_answer(res,user)                             # сохраняем в бд
    # await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'твой ответ {int(res)} ?',
    #                                     reply_markup=create_kb_mult(int(res)))
    await bot.edit_message_media(media=InputMediaPhoto(media=settings.PICTURE, caption=f'твой ответ {int(res)}?'),
                                 chat_id=chat_id,
                                 message_id=message_id, reply_markup=create_kb_mult100(int(res)))




@dp.message_handler(content_types=['sticker'])
async def find_sticker_id(message: Message):
    print(message.as_json())
    print(message.sticker.file_id)