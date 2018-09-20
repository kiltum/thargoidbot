#!/usr/bin/env python


#  pip3 install python-telegram-bot --upgrade

import json
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import logging

config = json.loads("{}")

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
    bot.send_message(chat_id=update.message.chat_id, text="Привет! Я один из таргоидов, поэтому не доставайте меня")

def message(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
    print(update)
    print(update.message.chat.id)
    print(update.message.chat.type)

def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Чё?")

def main():
    if configLoad("config.json") != True:
        print("I need config.json")
        exit(1)

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

    updater.start_polling()



if __name__ == "__main__":
    main()
