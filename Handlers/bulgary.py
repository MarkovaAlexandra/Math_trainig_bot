from aiogram.types import  Message, CallbackQuery, InputMediaPhoto
from loader import dp, bot
from Keyboard import create_main_menu
from Keyboard.callback import callback
from DataBase import new_user, check_user
import settings

@dp.message_handler(commands=['bulgary'])
async def bulgary(message: Message):
    await message.answer('yes, Bulgaria')