from aiogram.types import  Message, CallbackQuery
from loader import dp, bot
from Keyboard import buttons,create_buttons,create_main_menu
from Keyboard.callback import callback
from DataBase import new_user, check_user

@dp.callback_query_handler(callback.filter(btn='main'))
@dp.message_handler(commands=['start'])
async def greet_user(message: Message | CallbackQuery):
    if isinstance(message, Message):
        id = message.from_user.id
        await message.answer(f'Приветствую, {message.from_user.first_name}', reply_markup=create_main_menu()),
        print(check_user(id))
        print(type(check_user(id)))
        if check_user(id) == None:
            new_user(id)
    #await bot.send_message(477720457, f'к чату присоединился {message.from_user.first_name}')



    else:
        message_id = message.message.message_id
        chat_id = message.message.chat.id
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id,text='OK',
                                    reply_markup=create_main_menu())
