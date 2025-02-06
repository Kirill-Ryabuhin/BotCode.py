import telebot
from telebot import types
import sqlite3
import random
import webbrowser
from dotenv import load_dotenv
import os
import requests

load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN'), parse_mode=None)


nickname = None
user_pass = None

@bot.message_handler(content_types=['voice'])
def get_audio(message):
    bot.reply_to(message, 'Я не понимаю что ты говоришь, кожанный ублюдок')

@bot.message_handler(content_types=['photo'])
def get_pickture(message):
    bot.reply_to(message, 'Если это не дикпик, то даже смотреть не буду')

@bot.message_handler(commands=['start'])    
def start(message):
    connection = sqlite3.connect('list_of_users.sql')
    cur = connection.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar (50), pass varchar(50))')
    connection.commit()
    cur.close()
    connection.close()
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}, "Для регистрации введите свой ник в Dota2" ')
    bot.register_next_step_handler(message, user_name)


def user_name(message):
    global nickname
    nickname = message.text.strip()
    bot.send_message(message.chat.id, "придумай и введи пароль")
    bot.register_next_step_handler(message, user_password)


def user_password(message):
    global user_pass
    user_pass = message.text.strip()

    connection = sqlite3.connect('list_of_users.sql')
    cur = connection.cursor()
    cur.execute("INSERT INTO users (name, pass) VALUES ('%s', '%s')" % (nickname, user_pass))

    connection.commit()
    cur.close()
    connection.close()

    markup = types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='users'))
    bot.send_message(message.chat.id, 'Записал тебя в книжечку', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    connection = sqlite3.connect('list_of_users.sql')
    cur = connection.cursor()

    cur.execute('SELECT * FROM users')

    users = cur.fetchall()

    info = ''
    for el in users:
        info += f'Имя: {el[1] }'

    cur.close()
    connection.close()

    bot.send_message(call.message.chat.id, info)


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'Спроси меня "бот за кого сыграть"')


stat = requests.get(f'https://api.opendota.com/api/heroStats')
stat_j = stat.json()

win_re = []
for match in stat_j:
    win_re.append(match["pub_win"] / match["pub_pick"])


heroes = requests.get(f'https://api.opendota.com/api/heroes')
data = heroes.json()

list_of_heroes = []

for dictionary in data:
    if dictionary["localized_name"] not in list_of_heroes:
        list_of_heroes.append(dictionary["localized_name"])


@bot.message_handler(content_types=['text'])
def info(message):
    if message.text.lower() == "бот за кого сыграть":
        bot.reply_to(message, random.choices(population=list_of_heroes, weights=win_re, k=1)[0])
    else:
        bot.reply_to(message, "я только подсказываю за кого сыграть, за остальным обращайся к своему мозгу, если он есть")



bot.polling(non_stop=True)
