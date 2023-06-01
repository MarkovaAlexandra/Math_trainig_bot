from aiogram.types import  Message
from loader import dp

@dp.message_handler(commands=['help'])
async def help_command(message:Message):
    await message.answer('решай примеры, получай котиков, и мама тебя похвалит')