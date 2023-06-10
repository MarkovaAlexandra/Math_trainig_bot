


from loader import dp, bot
import random
from Keyboard import create_kb_plus,create_kb_plus100,create_kb_mult, create_kb_mult100, \
    create_kb_div100, create_kb_div10, create_kb_dif10,create_kb_dif100

from aiogram.types import Message, CallbackQuery, InputMediaPhoto
import settings
from Keyboard.callback import callback
from DataBase import update_user_answer,update_bot_answer,check_user_answer
#
#
@dp.callback_query_handler(callback.filter(menu='main_plus_10'))
async def enter(call: CallbackQuery):
    user = call.from_user.id
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    res = str(check_user_answer(user)[0])                    # из бд берем текущий результат
    _, operation, num = call.data.split(':')
    if num.isdigit():
         res += num                                           # и конкатинируем
    else:
        if len(res)==1:
            res = 0
        else:
            res = res[:-1]
    update_user_answer(res,user)                             # сохраняем в бд


    if operation == 'answer_plus':
        keybord = create_kb_plus(int(res))

    if operation == 'answer_mult':
         keybord = create_kb_mult(int(res))

    if operation == 'answer_mult100':
        keybord = create_kb_mult100(int(res))

    if operation == 'answer_plus100':
         keybord = create_kb_plus100(int(res))

    if operation == 'answer_dif10':
        keybord = create_kb_dif10(int(res))

    if operation == 'answer_dif100':
        keybord = create_kb_dif100(int(res))


    if operation == 'answer_div10':
        keybord = create_kb_div10(int(res))

    if operation == 'answer_div100':
        keybord = create_kb_div100(int(res))

    # else:
    #     keybord = create_kb_plus


    await bot.edit_message_media(media=InputMediaPhoto(media=settings.PICTURE, caption=f'твой ответ {int(res)}?'),
                                  chat_id=chat_id,
                                 message_id=message_id, reply_markup=keybord)

