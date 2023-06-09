from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton as InKB
from .callback import callback



def create_buttons() -> ReplyKeyboardMarkup:
    keybord = ReplyKeyboardMarkup(resize_keyboard=True)
    btn_plus = KeyboardButton(text='/plus')
    btn_multipl = KeyboardButton(text='/multipl')
    btn_help = KeyboardButton(text='/help')
    btn_love = KeyboardButton(text='/sasha_is_the_best')

    keybord.add(btn_plus,btn_multipl,btn_help, btn_love)
    return keybord

def create_main_menu() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=2)
    btn_plus_up10 = InKB(text='сложение до 10',callback_data=callback.new(menu='plus_up10', btn='plus_up10'))
    btn_mult_up10 = InKB(text='таблица умножения', callback_data=callback.new(menu='mult_up10',btn='mult_up10'))
    btn_plus_up100 = InKB(text='сложение многозначных', callback_data=callback.new(menu='plus_up100',btn='plus_up100'))
    btn_mult_up100 = InKB(text='умножение многозначных', callback_data=callback.new(menu='mult_up100', btn='mult_up100'))
    btn_dif_up10 = InKB(text='вычитание до 10', callback_data=callback.new(menu='dif_up10', btn='dif_up10'))
    btn_dif_up100 = InKB(text='вычитание до 100', callback_data=callback.new(menu='dif_up100', btn='dif_up100'))
    btn_div_up10 = InKB(text='деление табличное', callback_data=callback.new(menu='div_up10', btn='div_up10'))
    btn_div_up100 = InKB(text='деление многозначных', callback_data=callback.new(menu='div_up100', btn='div_up100'))

    keyboard.add(btn_plus_up10,  btn_plus_up100,btn_mult_up10,btn_mult_up100,btn_dif_up10,btn_dif_up100,
                 btn_div_up10,btn_div_up100)
    return keyboard
