from aiogram.types import InlineKeyboardButton as InKB, InlineKeyboardMarkup
from .callback import callback


def create_kb_plus(enter: int):
    normalnaya('main_plus_10')
    keyboard = normalnaya('main_plus_10')
    btn_del = InKB(text='отмена', callback_data=callback.new(menu='main_plus_10', btn='del'))
    btn_enter_plus = InKB(text='подтвердить', callback_data=callback.new(menu='answer_plus', btn=f'{enter}'))
    btn_back = InKB(text='к темам', callback_data=callback.new(menu='', btn='main'))
    keyboard.row(btn_del, btn_enter_plus, btn_back)
    return keyboard


def create_kb_plus100(enter: int):

    keyboard = normalnaya('main_plus_100')
    btn_del = InKB(text='отмена',callback_data=callback.new(menu='main_plus100', btn='del'))
    btn_enter_plus = InKB(text='подтвердить', callback_data=callback.new(menu='answer_plus100',btn=f'{enter}'))
    btn_back = InKB(text='к темам', callback_data=callback.new(menu='', btn='main'))
    keyboard.row(btn_del, btn_enter_plus, btn_back)
    return keyboard


def create_kb_mult(enter: int):

    keyboard = normalnaya('main_mult_10')
    btn_del = InKB(text='отмена',callback_data=callback.new(menu='main', btn='del'))
    btn_enter_mult = InKB(text='подтвердить', callback_data=callback.new(menu='answer_mult',btn=f'{enter}'))
    btn_back = InKB(text='к темам', callback_data=callback.new(menu='', btn='main'))
    keyboard.row(btn_del, btn_enter_mult, btn_back)
    return keyboard

def create_kb_mult100(enter: int):

    keyboard = normalnaya('main_mult_100')
    btn_del = InKB(text='отмена',callback_data=callback.new(menu='main_mult100', btn='del'))
    btn_enter_mult = InKB(text='подтвердить', callback_data=callback.new(menu='answer_mult100',btn=f'{enter}'))
    btn_back = InKB(text='к темам', callback_data=callback.new(menu='', btn='main'))
    keyboard.row(btn_del, btn_enter_mult, btn_back)
    return keyboard

def create_kb_dif10(enter: int):

    keyboard = normalnaya('main_dif_10')
    btn_del = InKB(text='отмена',callback_data=callback.new(menu='main_dif10', btn='del'))
    btn_enter_mult = InKB(text='подтвердить', callback_data=callback.new(menu='answer_dif10',btn=f'{enter}'))
    btn_back = InKB(text='к темам', callback_data=callback.new(menu='', btn='main'))
    keyboard.row(btn_del, btn_enter_mult, btn_back)
    return keyboard


def create_kb_div10(enter: int):

    keyboard = normalnaya('main_div10')
    btn_del = InKB(text='отмена',callback_data=callback.new(menu='main_div10', btn='del'))
    btn_enter_mult = InKB(text='подтвердить', callback_data=callback.new(menu='answer_div10',btn=f'{enter}'))
    btn_back = InKB(text='к темам', callback_data=callback.new(menu='', btn='main'))
    keyboard.row(btn_del, btn_enter_mult, btn_back)
    return keyboard


def create_kb_dif_100(enter: int):

    keyboard = normalnaya('main_dif_100')
    btn_del = InKB(text='отмена',callback_data=callback.new(menu='main_dif_100', btn='del'))
    btn_enter_mult = InKB(text='подтвердить', callback_data=callback.new(menu='answer_dif100',btn=f'{enter}'))
    btn_back = InKB(text='к темам', callback_data=callback.new(menu='', btn='main'))
    keyboard.row(btn_del, btn_enter_mult, btn_back)
    return keyboard

def create_kb_div100(enter: int):

    keyboard = normalnaya('main_div100')
    btn_del = InKB(text='отмена',callback_data=callback.new(menu='main_div100', btn='del'))
    btn_enter_mult = InKB(text='подтвердить', callback_data=callback.new(menu='answer_div100',btn=f'{enter}'))
    btn_back = InKB(text='к темам', callback_data=callback.new(menu='', btn='main'))
    keyboard.row(btn_del, btn_enter_mult,btn_back)
    return keyboard

def create_nex_plus_pos():
    keybord_a = InlineKeyboardMarkup()
    btn_next_plus = InKB(text='дальше',callback_data=callback.new(menu='',btn='next_plus'))
    btn_back = InKB(text='к темам',callback_data=callback.new(menu='',btn='main'))
    keybord_a.add(btn_next_plus,btn_back)
    return keybord_a

def create_nex_plus_pos_100():
    keybord = InlineKeyboardMarkup()
    btn_next_plus = InKB(text='дальше',callback_data=callback.new(menu='',btn='next_plus_100'))

    btn_back = InKB(text='к темам',callback_data=callback.new(menu='',btn='main'))
    keybord.add(btn_next_plus,btn_back)
    return keybord


def create_nex_mult_pos():
    keybord = InlineKeyboardMarkup()
    btn_next_mult = InKB(text='дальше',callback_data=callback.new(menu='',btn='next_mult'))
    btn_back = InKB(text='к темам', callback_data=callback.new(menu='', btn='main'))
    keybord.add(btn_next_mult,btn_back)
    return keybord

def create_nex_mult_pos100():
    keybord = InlineKeyboardMarkup()
    btn_next_mult = InKB(text='дальше',callback_data=callback.new(menu='',btn='next_mult100'))
    btn_back = InKB(text='к темам', callback_data=callback.new(menu='', btn='main'))
    keybord.add(btn_next_mult,btn_back)
    return keybord

def create_nex_dif10():
    keybord = InlineKeyboardMarkup()
    btn_next_mult = InKB(text='дальше',callback_data=callback.new(menu='',btn='next_dif10'))
    btn_back = InKB(text='к темам', callback_data=callback.new(menu='', btn='main'))
    keybord.add(btn_next_mult, btn_back)
    return keybord

def create_nex_div10():
    keybord = InlineKeyboardMarkup()
    btn_next_mult = InKB(text='дальше',callback_data=callback.new(menu='',btn='next_div10'))
    btn_back = InKB(text='к темам', callback_data=callback.new(menu='', btn='main'))
    keybord.add(btn_next_mult, btn_back)
    return keybord

def create_nex_dif100():
    keybord = InlineKeyboardMarkup()
    btn_next_mult = InKB(text='дальше',callback_data=callback.new(menu='',btn='next_dif100'))

    btn_back = InKB(text='к темам', callback_data=callback.new(menu='', btn='main'))
    keybord.add(btn_next_mult,btn_back)
    return keybord

def create_nex_div100():
    keybord = InlineKeyboardMarkup()
    btn_next_mult = InKB(text='дальше',callback_data=callback.new(menu='',btn='next_div100'))
    btn_back = InKB(text='к темам', callback_data=callback.new(menu='', btn='main'))
    keybord.add(btn_next_mult, btn_back)
    return keybord


def klaviatura_dura():
    keybord = InlineKeyboardMarkup()
    btn_1 = InKB(text='кнопка1', callback_data=callback.new(menu='', btn = 'knopka1'))
    btn_2 = InKB(text='кнопка2', callback_data=callback.new(menu='', btn='knopka2'))
    keybord.add(btn_1,btn_2)
    return keybord


def normalnaya(menu: str):
    keyboard = InlineKeyboardMarkup()
    btn_1 = InKB(text='1',callback_data=callback.new(menu=menu, btn=1))
    btn_2 = InKB(text='2',callback_data=callback.new(menu=menu, btn=2))
    btn_3 = InKB(text='3',callback_data=callback.new(menu=menu, btn=3))
    btn_4 = InKB(text='4',callback_data=callback.new(menu=menu, btn=4))
    btn_5 = InKB(text='5',callback_data=callback.new(menu=menu, btn=5))
    btn_6 = InKB(text='6',callback_data=callback.new(menu=menu, btn=6))
    btn_7 = InKB(text='7',callback_data=callback.new(menu=menu, btn=7))
    btn_8 = InKB(text='8',callback_data=callback.new(menu=menu, btn=8))
    btn_9 = InKB(text='9',callback_data=callback.new(menu=menu, btn=9))
    btn_0 = InKB(text='0',callback_data=callback.new(menu=menu, btn=0))
    keyboard.row(btn_1, btn_2, btn_3, btn_4, btn_5)
    keyboard.row(btn_6, btn_7, btn_8, btn_9, btn_0)
    return keyboard



