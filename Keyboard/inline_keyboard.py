from aiogram.types import InlineKeyboardButton as InKB, InlineKeyboardMarkup
from .callback import callback


def create_kb_plus(enter: int):
    keyboard = InlineKeyboardMarkup(row_width=5)
    btn_1 = InKB(text='1',callback_data=callback.new(menu='main_plus', btn=1))
    btn_2 = InKB(text='2',callback_data=callback.new(menu='main_plus', btn=2))
    btn_3 = InKB(text='3',callback_data=callback.new(menu='main_plus', btn=3))
    btn_4 = InKB(text='4',callback_data=callback.new(menu='main_plus', btn=4))
    btn_5 = InKB(text='5',callback_data=callback.new(menu='main_plus', btn=5))
    btn_6 = InKB(text='6',callback_data=callback.new(menu='main_plus', btn=6))
    btn_7 = InKB(text='7',callback_data=callback.new(menu='main_plus', btn=7))
    btn_8 = InKB(text='8',callback_data=callback.new(menu='main_plus', btn=8))
    btn_9 = InKB(text='9',callback_data=callback.new(menu='main_plus', btn=9))
    btn_0 = InKB(text='0',callback_data=callback.new(menu='main_plus', btn=0))
    btn_del = InKB(text='отмена',callback_data=callback.new(menu='main_plus', btn='del'))
    btn_enter_plus = InKB(text='подтвердить', callback_data=callback.new(menu='answer_plus',btn=f'{enter}'))
    keyboard.row(btn_1,btn_2,btn_3,btn_4,btn_5)
    keyboard.row(btn_6,btn_7,btn_8,btn_9,btn_0)
    keyboard.row(btn_del, btn_enter_plus)
    return keyboard

def create_kb_mult(enter: int):
    keyboard = InlineKeyboardMarkup(row_width=5)
    btn_1 = InKB(text='1',callback_data=callback.new(menu='main_mult', btn=1))
    btn_2 = InKB(text='2',callback_data=callback.new(menu='main_mult', btn=2))
    btn_3 = InKB(text='3',callback_data=callback.new(menu='main_mult', btn=3))
    btn_4 = InKB(text='4',callback_data=callback.new(menu='main_mult', btn=4))
    btn_5 = InKB(text='5',callback_data=callback.new(menu='main_mult', btn=5))
    btn_6 = InKB(text='6',callback_data=callback.new(menu='main_mult', btn=6))
    btn_7 = InKB(text='7',callback_data=callback.new(menu='main_mult', btn=7))
    btn_8 = InKB(text='8',callback_data=callback.new(menu='main_mult', btn=8))
    btn_9 = InKB(text='9',callback_data=callback.new(menu='main_mult', btn=9))
    btn_0 = InKB(text='0',callback_data=callback.new(menu='main_mult', btn=0))
    btn_del = InKB(text='отмена',callback_data=callback.new(menu='main_mult', btn='del'))
    btn_enter_mult = InKB(text='подтвердить', callback_data=callback.new(menu='answer_mult',btn=f'{enter}'))
    keyboard.row(btn_1,btn_2,btn_3,btn_4,btn_5)
    keyboard.row(btn_6,btn_7,btn_8,btn_9,btn_0)
    keyboard.row(btn_del, btn_enter_mult)
    return keyboard


def create_nex_plus_pos():
    keybord_a = InlineKeyboardMarkup()
    btn_next_plus = InKB(text='дальше',callback_data=callback.new(menu='',btn='next_plus'))
    btn_smile = InKB(text='smile',callback_data=callback.new(menu='',btn='smile'))
    btn_back = InKB(text='назад',callback_data=callback.new(menu='',btn='main'))
    keybord_a.add(btn_smile,btn_next_plus,btn_back)
    return keybord_a


def create_nex_mult_pos():
    keybord_b = InlineKeyboardMarkup()
    btn_next_mult = InKB(text='дальше',callback_data=callback.new(menu='',btn='next_mult'))
    btn_smile = InKB(text='smile',callback_data=callback.new(menu='',btn='smile'))
    btn_back = InKB(text='назад', callback_data=callback.new(menu='', btn='main'))
    keybord_b.add(btn_smile,btn_next_mult,btn_back)
    return keybord_b