from aiogram.types import Message
from loader import dp, bot
from aiogram.dispatcher import filters
import random
import time
from Keyboard import create_kb_mult, create_nex_mult_pos
from aiogram.types import Message, CallbackQuery
import settings
from Keyboard.callback import callback



@dp.callback_query_handler(callback.filter(btn='next_mult'))
@dp.callback_query_handler(callback.filter(menu='mult_up10'))
#@dp.message_handler(commands=['multipl'])
async def multipl(message: Message | CallbackQuery):
    user = message.from_user.id
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    settings.RESULT = a * b

    message_id = message.message.message_id
    chat_id = message.message.chat.id
    await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                    text=f'{a} * {b} = ?', reply_markup=create_kb_mult(settings.ENTER))

@dp.callback_query_handler(callback.filter(menu='main_mult'))
async def enter(call: CallbackQuery):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    _, _, num = call.data.split(':')
    if num.isdigit():
        settings.ENTER += num
    else:
        settings.ENTER = settings.ENTER[:-1]
    await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'твой ответ {settings.ENTER} ?',
                                        reply_markup=create_kb_mult(settings.ENTER))

# @dp.callback_query_handler(callback.filter(menu=['answer_plus', 'answer_mult']))
# async def proverka(call: CallbackQuery):
#     print(f' тут печатаю дату {call.data}')
#     _, _, settings.ENTER = call.data.split(':')
#     user = call.from_user.id
#     chat_id = call.message.chat.id
#     message_id = call.message.message_id
#     if settings.RESULT == int(settings.ENTER):
#         await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='Молодец',
#                                             reply_markup=create_nex_mult_pos())
#
#     else:
#         await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
#                                             text=f'ничего подобного, верный ответ {settings.RESULT}',
#                                             reply_markup=create_nex_mult_pos())
#     settings.ENTER = ''














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
