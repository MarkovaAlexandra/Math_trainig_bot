

from loader import dp, bot
import random
from Keyboard import create_kb_plus
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
import settings
from Keyboard.callback import callback
from DataBase import update_bot_answer, update_user_answer,check_user_answer


@dp.callback_query_handler(callback.filter(btn='next_plus'))
@dp.callback_query_handler(callback.filter(menu='plus_up10'))
async def plus(message: Message | CallbackQuery):

    user = message.from_user.id
    message_id = message.message.message_id
    chat_id = message.message.chat.id
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    result = a + b
    update_bot_answer(result, user)                                 # вношу в бд правильный ответ
    await bot.edit_message_media(media=InputMediaPhoto(media=settings.PICTURE, caption=f'{a} + {b} = ?'), chat_id=chat_id,
                                 message_id=message_id, reply_markup=(create_kb_plus(settings.ENTER)))

# @dp.callback_query_handler(callback.filter(menu='main'))
# async def enter(call: CallbackQuery):
#     user = call.from_user.id
#     chat_id = call.message.chat.id
#     message_id = call.message.message_id
#     res = str(check_user_answer(user)[0])                           # текущее значение из бд
#     print(call.data)
#     _, _, num = call.data.split(':')
#     if num.isdigit():
#         res += num                                                  # к текущему значению в бд конкатинировали num
#     else:
#         if len(res) == 1:
#             res = 0
#         else:
#             res = res[:-1]                                          # от текущего значение отрезали последнюю цифру
#     update_user_answer(int(res), user)                              # и обновили его в бд
#     await bot.edit_message_media(media=InputMediaPhoto(media=settings.PICTURE, caption=f'твой ответ {int(res)}?'),
#                                  chat_id=chat_id,
#                                  message_id=message_id,
#                                  reply_markup=create_kb_plus(int(res)))






