from aiogram.types import Message
from loader import dp, bot
from aiogram.dispatcher import filters
import random
import time
from Keyboard import create_kb_plus, create_nex_plus_pos,create_nex_mult_pos
from aiogram.types import Message, CallbackQuery
import settings
from Keyboard.callback import callback
from DataBase import update_user_answer, check_user_answer, refresh_user_answer




@dp.callback_query_handler(callback.filter(menu=['answer_plus', 'answer_mult']))
async def proverka(call: CallbackQuery):
    '''
    Проверяем ответ юзера и арифметичское действие, которое он делал, чтобы при нажатии дальше
    он перешел к тем же типам примеров, для этого из call.data вытаскиваю ответ и арифм.действие
    :param call:
    :return: клавиатуру с кнопкой ответа на арифм.действие
    '''
    print(f' тут печатаю дату {call.data}')
    # _, operation, settings.ENTER = call.data.split(':')
    # user_result = settings.ENTER
    _,operation,user_result = call.data.split(':')
    if operation == 'answer_plus':
        return_keybord = create_nex_plus_pos
    if operation == 'answer_mult':
        return_keybord = create_nex_mult_pos
    user = call.from_user.id
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    update_user_answer(user_result,user) # вношу в бд ответ юзера
    print(check_user_answer(user))
    print(type(check_user_answer(user)))
    results = check_user_answer(user)
    print(results[0])
    print(results[1])
    if results[0]==results[1]:
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='Молодец',
                                    reply_markup=return_keybord())

    # if settings.RESULT == int(settings.ENTER):
    #     await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='Молодец',
    #                                         reply_markup=return_keybord())
    else:
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                            text=f'ничего подобного, верный ответ {results[1]}',
                                            reply_markup=return_keybord())
    settings.ENTER = ''
    refresh_user_answer(user)