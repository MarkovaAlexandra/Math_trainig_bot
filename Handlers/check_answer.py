

from loader import dp, bot
from Keyboard import  create_nex_plus_pos,create_nex_mult_pos, create_nex_plus_pos_100, \
    create_nex_mult_pos100, create_nex_dif10, create_nex_dif100, create_nex_div10, create_nex_div100
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
import settings
from Keyboard.callback import callback
from DataBase import update_user_answer, check_user_answer, refresh_user_answer, update_statistics




@dp.callback_query_handler(callback.filter(menu=['answer_plus', 'answer_mult','answer_plus100',
                                                 'answer_mult100', 'answer_dif10', 'answer_dif100',
                                                 'answer_div10', 'answer_div100']))
async def proverka(call: CallbackQuery):
    '''
    Проверяем ответ юзера и арифметичское действие, которое он делал, чтобы при нажатии "дальше"
    он перешел к тем же типам примеров, для этого из call.data вытаскиваю ответ и арифм.действие
    :param call:
    :return: клавиатуру с кнопкой ответа на арифм.действие
    '''

    _,operation,user_result = call.data.split(':')
    print(call.data)
    if operation == 'answer_plus':
        return_keybord = create_nex_plus_pos
        column_rights = 'plus10rights'
        column_mistakes = 'plus10mistakes'
    if operation == 'answer_mult':
        return_keybord = create_nex_mult_pos
        column_rights = 'mult10rights'
        column_mistakes = 'mult10mistakes'
    if operation == 'answer_mult100':
        return_keybord = create_nex_mult_pos100
        column_rights = 'mult100rights'
        column_mistakes = 'mult100mistakes'
    if operation == 'answer_plus100':
        return_keybord = create_nex_plus_pos_100
        column_rights = 'plus100rights'
        column_mistakes = 'plus100mistakes'
    if operation == 'answer_dif10':
        return_keybord = create_nex_dif10
        column_rights = 'diff10rights'
        column_mistakes = 'diff10mistakes'
    if operation == 'answer_dif100':
        return_keybord = create_nex_dif100
        column_rights = 'diff100rights'
        column_mistakes = 'diff100mistakes'

    if operation == 'answer_div10':
        return_keybord = create_nex_div10
        column_rights = 'div10rights'
        column_mistakes = 'div10mistakes'
    if operation == 'answer_div100':
        return_keybord = create_nex_div100
        column_rights = 'div100rights'
        column_mistakes = 'div100mistakes'

    user = call.from_user.id
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    update_user_answer(user_result,user) # вношу в бд ответ юзера
    results = check_user_answer(user)
    if results[0]==results[1]:
        update_statistics(user,column_rights)

        await bot.edit_message_media(media=InputMediaPhoto(media=settings.PICTURE_RIGHT, caption='Молодец'),
                                     chat_id=chat_id,
                                     message_id=message_id, reply_markup=return_keybord())

    else:
        update_statistics(user,column_mistakes)

        await bot.edit_message_media(media=InputMediaPhoto(media=settings.PICTURE_WRONG,
                                    caption=f'ничего подобного, верный ответ {results[1]}'),
                                     chat_id=chat_id,
                                     message_id=message_id, reply_markup=return_keybord())
    refresh_user_answer(user)