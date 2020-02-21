#-*- coding: utf-8 -*-
import telebot
from telebot import *

import keyboards
from keyboards import *

import config
from config import *
bot = telebot.TeleBot(TOKEN)


"""
markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
itembtn1 = types.KeyboardButton('MO')
itembtn2 = types.KeyboardButton('Button number 2')
itembtn3 = types.KeyboardButton('Button number 3')
markup.add(itembtn1, itembtn2, itembtn3)"""


@bot.message_handler(commands=['start'])
def start_message(message):
#    bot.send_message(message.chat.id, 'Привет, '+ message.from_user.first_name)
    bot.reply_to(message, 'Helloss, '+ str(message.from_user.first_name), reply_markup=markup)

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'This is help information')

#@bot.message_handler(command=['file'])
#def file_message(message):


@bot.message_handler(func=lambda message: True, content_types=['text'])
def send_text(message):
    if message.text == 'MO':
        bot.send_message(message.chat.id, "https://drive.google.com/uc?export=download&id=13EjoZIFmyZm9heGAdMZbou0k0BIh3dvi")
    elif message.text == 'Bye':
        bot.send_message(message.chat.id, "good bye")
    else :
        bot.send_message(message.chat.id, "Sorry, i dont understand you.")

bot.polling(none_stop=True, interval=0)






"""
@bot.message_handler(commands=['geophone'])
def geophone(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=4, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_phone, button_geo)
    bot.send_message(message.chat.id, "Отправь мне свой номер телефона или поделись местоположением, жалкий человечишка!", reply_markup=keyboard)
"""
