from aiogram.types import Message
from loader import dp, bot
from aiogram.dispatcher import filters
import random
import time
from Keyboard import create_kb_plus, create_nex_plus_pos,create_nex_mult_pos
from aiogram.types import Message, CallbackQuery
import settings
from Keyboard.callback import callback
from DataBase import update_user_answer, check_user_answer, refresh_user_answer, update_statistics




@dp.callback_query_handler(callback.filter(menu=['answer_plus', 'answer_mult']))
async def proverka(call: CallbackQuery):
    '''
    Проверяем ответ юзера и арифметичское действие, которое он делал, чтобы при нажатии "дальше"
    он перешел к тем же типам примеров, для этого из call.data вытаскиваю ответ и арифм.действие
    :param call:
    :return: клавиатуру с кнопкой ответа на арифм.действие
    '''

    _,operation,user_result = call.data.split(':')
    if operation == 'answer_plus':
        return_keybord = create_nex_plus_pos
        column_rights = 'plus10rights'
        column_mistakes = 'plus10mistakes'
    if operation == 'answer_mult':
        return_keybord = create_nex_mult_pos
        column_rights = 'mult10rights'
        column_mistakes = 'mult10mistakes'
    user = call.from_user.id
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    update_user_answer(user_result,user) # вношу в бд ответ юзера
    results = check_user_answer(user)
    if results[0]==results[1]:
        update_statistics(user,column_rights)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='Молодец',
                                    reply_markup=return_keybord())
    else:
        update_statistics(user,column_mistakes)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                            text=f'ничего подобного, верный ответ {results[1]}',
                                            reply_markup=return_keybord())
#    settings.ENTER = ''
    refresh_user_answer(user)