from aiogram.types import Message
from loader import dp, bot
from aiogram.dispatcher import filters
import random
import time
from Keyboard import create_kb_plus, create_nex_plus_pos,create_nex_mult_pos
from aiogram.types import Message, CallbackQuery
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
    await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                  text=f'{a} + {b} = ?',reply_markup=create_kb_plus(settings.ENTER))


@dp.callback_query_handler(callback.filter(menu='main_plus'))
async def enter(call: CallbackQuery):
    user = call.from_user.id
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    res = str(check_user_answer(user)[0])                           # текущее значение из бд
    _, _, num = call.data.split(':')
    if num.isdigit():
        res += num                                                  # к текущему значению в бд конкатинировали num
    else:
        res = res[:-1]                                              # от текущего значение отрезали последнюю цифру
    update_user_answer(int(res), user)                              # и обновили его в бд
    await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'твой ответ {int(res)}?',
                                        reply_markup=create_kb_plus(int(res)))








@dp.callback_query_handler(callback.filter(menu='next_plus'))
async def next_plus(call: CallbackQuery):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    await plus(call.message)


@dp.callback_query_handler(callback.filter(menu='next_mult'))
async def next_mult(call: CallbackQuery):
    print('я тут')
    print(call)
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    await multipl(call.message)


@dp.message_handler(filters.Text(equals='дурак', ignore_case=True))
async def proba(message: Message):
    await message.reply('сам дурак')


@dp.message_handler(content_types=['sticker'])
async def find_sticker_id(message: Message):
    print(message.as_json())
    print(message.sticker.file_id)


