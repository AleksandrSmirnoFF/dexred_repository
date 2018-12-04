#!/usr/bin/venv python

import random
import telebot

from telebot.types import Message

TOKEN = '754710983:AAFGZWX25g2co2I4Y2Y4ggXHDEwxr_rinNI'

bot = telebot.TeleBot(TOKEN)

startSTR = "This is bot of DexRed company";
helpSTR = "Hello this is DexRed bot. Use /start to start"


@bot.message_handler(commands=['help'])
def command_handler(message: Message):
    bot.reply_to(message, helpSTR)


@bot.message_handler(commands=['start'])
def echo_digits(message: Message):
    bot.reply_to(message, startSTR)


bot.polling(timeout=60)
