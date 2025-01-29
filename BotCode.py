import telebot
from telebot import types
import random
import webbrowser

bot = telebot.TeleBot("7954757426:AAEzfIOqVP5R21UaN7p2wa_pCNrTKcDLF84", parse_mode=None)


@bot.message_handler(content_types=['voice'])
def get_audio(message):
    bot.reply_to(message, 'Я не понимаю что ты говоришь, кожанный ублюдок')

@bot.message_handler(content_types=['photo'])
def get_pickture(message):
    bot.reply_to(message, 'Если это не дикпик, то даже смотреть не буду')

@bot.message_handler(commands=['start'])    
def start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}, напиши "/Help" ')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'Спроси меня "бот за кого сыграть"')


play = [
        {'hero': 'Гуля',  'weight': 4},
        {'hero': 'Джагер', 'weight': 6},
        {'hero': 'Фантомка', 'weight': 3},
        {'hero': 'Вк', 'weight': 4},
        {'hero': 'Антимаг', 'weight': 1},
        {'hero': 'Свен', 'weight': 1},
        {'hero': 'Медуза', 'weight': 1}
]


heroes = list(map(lambda x: x['hero'], play))
weights = list(map(lambda x: x['weight'], play))


@bot.message_handler(content_types=['text'])
def info(message):
    if message.text.lower() == "бот за кого сыграть":
        bot.reply_to(message, random.choices(population=heroes, weights=weights, k=1)[0])
    elif message.text.lower() != "бот за кого сыграть":
        bot.reply_to(message, "я только подсказываю за кого сыграть, за остальным обращайся к своему мозгу, если он есть")



bot.polling(non_stop=True)
