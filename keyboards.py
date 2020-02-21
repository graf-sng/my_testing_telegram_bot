import telebot
from telebot import *
markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
itembtn1 = types.KeyboardButton('MO')
itembtn2 = types.KeyboardButton('Bye')
itembtn3 = types.KeyboardButton('Hello')
markup.add(itembtn1, itembtn2, itembtn3)
