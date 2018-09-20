#!/usr/bin/env python


#  pip3 install python-telegram-bot --upgrade

import json
import random
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.error import (TelegramError, Unauthorized, BadRequest,
                            TimedOut, ChatMigrated, NetworkError)
import logging

config = json.loads("{}")

reply_what_you_want=[]
reply_barnacle=[]


def initReply():
    global reply_what_you_want
    reply_what_you_want.append("Человечишко, чего тебе надо?")
    reply_what_you_want.append("Опять ты ...")
    reply_what_you_want.append("Человек - это прежде всего кожаный мешок с вкусной и питательной биомассой! Понял?")

    reply_barnacle.append("Не дам, самим мало!")
    reply_barnacle.append("Лети в Pleiades Sector OI-T C3-7 A 6  -42.77, -21.70 и получи лазером в твою непутевую башку")
    reply_barnacle.append("Pleiades Sector IX-S B4-4 B 1 -40.46, 25.81 Просканируй, получи свои 30 серебрянников и вали")
    reply_barnacle.append("Нафиг они тебе? Лети в maya и там бери свои Meta-Alloy пока не сожгли всех")

def configLoad(name):
    global config
    try:
        with open(name, 'r') as f:
            config = json.load(f)
            return True
    except (IOError, ValueError):
        config = json.loads("{}")
        return False

def configGet(name):
    global config
    if name not in config:
        return ""
    else:
        return config[name]


def start(bot, update):
    if update.message.chat.type == 'private':
        bot.send_message(chat_id=update.message.chat_id, text="Привет! Я один из таргоидов, поэтому не доставайте меня")

def message(bot, update):
    bot.send_message(chat_id=-265595051, text=str(update))
    if "эй, таргоид" in update.message.text:
        if "барнакл" in update.message.text:
            bot.send_message(chat_id=update.message.chat_id, text=random.choice(reply_barnacle),
                             reply_to_message_id=update.message.message_id)
        else:
            bot.send_message(chat_id=update.message.chat_id, text=random.choice(reply_what_you_want), reply_to_message_id=update.message.message_id)
    # bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
    # print(update)
    # print(update.message.chat.id)
    # print(update.message.chat.type)

def unknown(bot, update):
    if update.message.chat.type == 'private':
        bot.send_message(chat_id=update.message.chat_id, text="Чё?")

def error_callback(bot, update, error):
    try:
        raise error
    except Unauthorized:
        print("Unathorized")
        # remove update.message.chat_id from conversation list
    except BadRequest:
        print("BadRequest")
        # handle malformed requests - read more below!
    except TimedOut:
        print("TimedOut")
        # handle slow connection problems
    except NetworkError:
        print("NetworkError")
        # handle other connection problems
    except ChatMigrated as e:
        print("ChatMigrated")
        # the chat_id of a group has changed, use e.new_chat_id instead
    except TelegramError:
        print("telegramError")
        # handle all other telegram related errors


def main():
    if configLoad("config.json") != True:
        print("I need config.json")
        exit(1)

    initReply()

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    updater = Updater(token=configGet("token"))
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    message_handler = MessageHandler(Filters.text, message)
    dispatcher.add_handler(message_handler)

    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)

    dispatcher.add_error_handler(error_callback)

    print("Ready")

    updater.start_polling()
    updater.idle()



if __name__ == "__main__":
    main()
