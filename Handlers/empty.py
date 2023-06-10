from aiogram.types import  Message
from loader import dp
import time
from loader import bot

@dp.message_handler()
async def empty(message: Message):
    user = message.from_user.first_name
    chat_id = message.chat.id
    await bot.send_message(chat_id=chat_id, text=f'{user}, тебе надо тыкнуть в кнопочку, текст я все равно читать не умею ')
    time.sleep(3)


