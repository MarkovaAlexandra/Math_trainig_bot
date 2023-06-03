import sqlite3


connection = sqlite3.connect('DataBase/user_base.db')
cursor = connection.cursor()


# def create_users_table():
#     sql = '''CREATE TABLE IF NOT EXISTS new_users_results (user_id INTEGER , user_unswer INTEGER,
#     bot_unswer INTEGER, plus10_rights INTEGER, plus10_mistakes INTEGER, mult10_rights INTEGER,
#     mult10_mistakes INTEGER)'''
#     cursor.execute(sql)
#     connection.commit()


def check_user(tg_id: int):
    sql = '''SELECT user_id FROM new_user_result WHERE user_id=?'''
    return cursor.execute(sql, (tg_id,)).fetchone()

def new_user(tg_id: int):
    sql = '''INSERT INTO new_user_result (user_id) VALUES (?)'''
    cursor.execute(sql, (tg_id,))
    connection.commit()

def update_bot_answer(result:int, tg_id:int):
    sql = '''UPDATE new_user_result SET bot_answer=? WHERE user_id=?'''
    cursor.execute(sql,(result, tg_id))
    connection.commit()

def update_user_answer(result:int, tg_id:int):
    sql = '''UPDATE new_user_result SET user_answer=? WHERE user_id=?'''
    cursor.execute(sql, (result,tg_id))
    connection.commit()

def check_user_answer(tg_id: int):
    sql = '''SELECT user_answer, bot_answer FROM new_user_result WHERE user_id=?'''
    return cursor.execute(sql, (tg_id,)).fetchone()



def refresh_user_answer(tg_id:int):
    sql = '''UPDATE new_user_result SET user_answer=0 WHERE user_id=?'''
    cursor.execute(sql, (tg_id,))
    connection.commit()

def update_statistics(tg_id:int, column:str):
    sql = f'''UPDATE new_user_result SET {column}={column} + 1 WHERE user_id=?'''
    print(sql)
    print(tg_id)
    cursor.execute(sql, (tg_id,))
    connection.commit()


# def update_statistics(tg_id:int):
#     sql = '''UPDATE user_result SET plus10rights=plus10rights + 1 WHERE user_id=?'''
#     print(sql)
#     print(tg_id)
#     cursor.execute(sql, (tg_id,))
#     connection.commit()