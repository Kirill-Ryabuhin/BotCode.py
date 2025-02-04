import os
import telebot
import random
import requests
import json
from telebot import types

s = requests.get(f'https://api.opendota.com/api/heroStats')
j = s.json()
print(j)
# надо взять из этих данных строчки pub_pick и pub_win сделать из них win_rate и потом вместе
# с листом героев подставить в функцию рандомайза в основной код

heroes = requests.get(f'https://api.opendota.com/api/heroes')
data = heroes.json()

list_of_heroes: list = ['Не сегодня', 'удали доту']
print(list_of_heroes)

for dictionary in data:
    if dictionary["localized_name"] not in list_of_heroes:
        list_of_heroes.append(dictionary["localized_name"])
print(list_of_heroes)
