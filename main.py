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

reply_what_you_want = []
reply_barnacle = []
places = []
killer = []
rules = []


def initReply():
    global reply_what_you_want
    global reply_barnacle
    global places
    global killer
    global rules

    reply_what_you_want.append("Человечишко, чего тебе надо?")
    reply_what_you_want.append("Опять ты ...")
    reply_what_you_want.append("Человек - это прежде всего кожаный мешок с вкусной и питательной биомассой! Понял?")
    reply_what_you_want.append("Я, как инсектоидная фемина, не рассматриваю тебя как партнера для спаривания! Лети отседа!")
    reply_what_you_want.append("Мои сердца мерцают не для тебя!")
    reply_what_you_want.append("Победили Защитников, растерзаем и вас ...")
    reply_what_you_want.append("Давно caustic damage не получал?")
    reply_what_you_want.append("И это весь твой Xeno Scanner? Такой маленький?")

    killer.append("И этим ты решил отплатить мне за все, что я для тебя сделала?")
    killer.append("Фи, меня этим не возьмешь!")
    killer.append("Редиска!")
    killer.append("Отсыпь еще, а?")

    rules.append("Будь человеком! Ведь это так вкусно!")
    rules.append("Не пиши часто, а то у меня головы болят")
    rules.append("Если ты агрессивен, то место тебе в клетке")
    rules.append("Политика это вам не тут, а вовсе даже в powerplay")
    rules.append("Хочешь повоевать? Сначала наточи свой лазер!")



    reply_barnacle.append("Не дам, самим мало!")
    reply_barnacle.append(
        "Лети в Pleiades Sector OI-T C3-7 A 6  -42.77, -21.70 и получи лазером в твою непутевую башку")
    reply_barnacle.append(
        "Pleiades Sector IX-S B4-4 B 1 -40.46, 25.81 Просканируй, получи свои 30 серебрянников и вали")
    reply_barnacle.append("Нафиг они тебе? Лети в MAIA и там бери свои Meta-Alloy пока не сожгли всех")

    places.append("Almeida Landing Conn A 3 A 73.3809 102.3764 (Added by CMDR. Piers Chip)")
    places.append("Barnacle California Sector LC-V c2-10 A 3 -17.3842 -18.7939 (Added by CMDR. Drygin)")
    places.append("Barnacle Pleiades Sector JC-U b3-2 1 21.3348 91.9834 (Added by CMDR. Drygin)")
    places.append("Barnacle Pleiades Sector JC-U b3-2 1 21.93 96.98 (Added by CMDR. Drygin)")
    places.append("Barnacle Merope 5 C -26.3515 -156.4056 (Added by CMDR. Drygin)")
    places.append("Barnacle Pleione 11 A 2.3189 177.2434 (Added by CMDR. Drygin)")
    places.append("Barnacle Outotz ST-I D9-6 Outotz ST-I D9-6 2A 76.233 -78.367 (Added by CMDR. Galdart)")
    places.append("Barnacles Pleiades Sector OI-T c3-7 B 4 -30.66 -36.37 (Added by CMDR. Light027)")
    places.append("Betterton Outpost HIP 19792 C 2 -24.7065 6.5560 (Added by Canonn Research)")
    places.append("Bug Killer Crashed Anaconda HIP 16613 1 A -11.0093 -95.6755 (Added by CMDR. Drygin)")
    places.append("Carmichael Point HIP 16824 A 2 73.8762 61.8761 (Added by CMDR. Drygin)")
    places.append("Clark Barrow's srv wreck HIP 16613 1 A -11.0962 -96.0339 (Added by CMDR. Sambal)")
    places.append("CMDR Jameson's Cobra MK3 HIP 12099 1 B -54.3 -50.3 (Added by CMDR. Drygin)")
    places.append("Comms Facility 89563 HR 1172 A 5 b -0.2508 -67.6809 (Added by CMDR. Bisador)")
    places.append("Crash site Hip 17403 A 4 A -34.98 -141.41 (Added by CMDR. V151on)")
    places.append("Crashed Anaconda Orrere 2 B 43.8214 -173.9800 (Added by Cannon Research Group)")
    places.append("Crashed Ananconda Koli Discii C 6 A 28.577 7.219 (Added by CMDR. Arkadius Dax)")
    places.append("Crashed Ship Col 285 sector TY-0 b20-6 1 a -55.39 175.03 (Added by CMDR. Moonfire)")
    places.append("Crashed Ship Garuda A 4 A 4.32 -144.62 (Added by CMDR. McNicholl)")
    places.append("Crashed Thargoid Scout HIP 17125 A 3 A -65.8193 48.8662 (Added by CMDR. twosuperdorks)")
    places.append("Crashed Thargoid Ship Pleiades Sector AB-W b2-4 9 A -26.3420 97.7335 (Added by CMDR. Drygin)")
    places.append("Dav's Hope Hyades Sector DR-V c2-23 A 5 44.8180 -31.3893 (Added by CMDR. Adingo)")
    places.append("Dixon Dock HR 2551 2 D -26.0807 -130.8341 (Added by Canonn Research)")
    places.append("Dominic’s Corner Pleiades Sector GW-W C1-15 12 a 5.5620 -116.7365 (Added by CMDR. Bisador)")
    places.append("Exploration Camp C-NO4 Synuefe JB-G B58-6 6 H -22.1371 177.6861 (Added by CMDR. RageInfinity)")
    places.append("Grave of Ships Carcosa AB 1 D -23.62 5.60 (Added by CMDR. McNicholl)")
    places.append(
        "Guardian Obelisk Data Synuefe NL-N C23-4 Synuefe NL-N C23-4 B 3 48.1805 -48.3719 (Added by CMDR. Russet Eveningshine)")
    places.append("Guardian Ruins Col 173 Sector XG-J C10-17 A 2 -17 44.24 (Added by CMDR. Ben Dofler)")
    places.append("Guardian Site SYNUEFE CE-R C21-6 C 1 42.155 72.61 (Added by Unknown)")
    places.append("Guardian site Col 173 Sector XG-J C10-17 A 2 -17 44.24 (Added by CMDR. Ben Dofler)")
    places.append("Guardian Structure Synuefe EU-Q c21-15 A 1 -111.61 37.80 (Added by CMDR. Drygin)")
    places.append("Guardian Structure Synuefe AH-J d10-20 A 3 98.44 -52.28 (Added by CMDR. Drygin)")
    places.append("Ivogog Hyades Sector DR-V c2-23 5 А 44.818 31.389 (Added by Unknown)")
    places.append("Jackson Enterprise Col 285 Sector YF-M c8-8 10 B 0.3905 33.5990 (Added by Canonn Research)")
    places.append("Lost anaconda hip 16613 1a -11.0093 -95.6755 (Added by CMDR. bluecrash)")
    places.append(
        "MegaBarnacle Hyades Sector AQ-Y D81 C 2 9.2924 -153.9186 (Added by CMDRs Lain Brigands, Kaz Archer and Panpiper)")
    places.append("Orion's Folly Col 285 Sector UZ-O c6-9 B 6 -87.0514 -10.5902 (Added by CMDR. Drygin)")
    places.append("Penal Colony BV-2259 HIP 16217 AB 1 a -55.0009 30.2834 (Added by CMDR. Bisador)")
    places.append("Plaa Aec TT-B b41-3 Plaa Aec TT-B b41-3 B 2 -9.3229 -103.8591 (Added by Canonn Research)")
    places.append("Research Base KG-3362 Pleiades Sector HR-W D1-17 1 a 58.1148 19.5427 (Added by CMDR. Bisador)")
    places.append("Research Facility 5592 HR 5591 1 b 33.4701 -2.1706 (Added by CMDR. ÔneRedBeard)")
    places.append("Scrump Landing Pleiades sector JN-S B4-3 2 -0.3434 12.9216 (Added by CMDR. Drygin)")
    places.append("Sensor fragments HIP 17403 A 4 A -34.98 -141.41 (Added by CMDR. WulffBane)")
    places.append("Sharpe Works Pleiades Sector IC-U B3-1 1 -4.9515 -85.7631 (Added by CMDR. Bisador)")
    places.append("Site 94 HIP 19284 A 2 -19.0622 -99.4450 (Added by CMDR. Drygin)")
    places.append("Stack HIP 12099 1 A -72.6561 -67.3629 (Added by CMDR. Drygin)")
    places.append("Stuart Retreat HIP 15329 A 3 C -62.6134 -44.2569 (Added by Canonn Research)")
    places.append("Thargoid Base HIP 19026 B 1 C -17 -152 (Added by CMDR. Falco Kendo)")
    places.append("Thargoid Base HIP 14909 2 A -26.4600 -27.4900 (Added by CMDR. Inqie)")
    places.append("Thargoid Cyclop crash site HIP 17403 A 4 A -34.9821 -141.4141 (Added by CMDR. TheFairy)")
    places.append("Type 9 Crash Site HIP 14840 2 41.10 -68.57 (Added by CMDR. KC9EYE)")
    places.append("Unidentified Wreckage Pekoe 9 A -5.08 95.03 (Added by CMDR. McNicholl)")
    places.append("Unidentified Wreckage Kopernik 7 A 22.78 74.06 (Added by CMDR. McNicholl)")
    places.append("Wreckage Edge Fraternity Landing A 2 19.83 171.23 (Added by CMDR. McNicholl)")


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


# var
#     calculateBearing = function()
#        {
#         var
#     t = $("#curLat").val(),
#          a = $("#curLon").val(),
#               e = $("#destLat").val(),
#                    o = $("#destLon").val();
#     t = t * Math.PI / 180, a = a * Math.PI / 180, e = e * Math.PI / 180;
#     var
#     n = (o = o * Math.PI / 180) - a,
#         i = Math.log(Math.tan(Math.PI / 4 + e / 2) / Math.tan(Math.PI / 4 + t / 2)),
#             l = Math.atan2(n, i) * (180 / Math.PI);
#     if (l < 0 & & (l = 360 + l), l = Math.round(l), isNaN(l))
#     return "<span style='color:red;'>X</span>";
#     $("#result").html(l + "&deg;")
#
# };


def start(bot, update):
    if update.message.chat.type == 'private':
        bot.send_message(chat_id=update.message.chat_id, text="Привет! Я один из таргоидов, поэтому не доставайте меня")


def message(bot, update):
    bot.send_message(chat_id=-265595051, text=str(update))
    # simple stupid AI simulator
    if "й, таргоид" in update.message.text:
        if "барнакл" in update.message.text:
            bot.send_message(chat_id=update.message.chat_id, text=random.choice(reply_barnacle),
                             reply_to_message_id=update.message.message_id)
        elif "летать" in update.message.text:
            bot.send_message(chat_id=update.message.chat_id, text=random.choice(places),
                             reply_to_message_id=update.message.message_id)
        elif "фос" in update.message.text:  # карбофос, дихлофос
            bot.send_message(chat_id=update.message.chat_id, text=random.choice(killer),
                             reply_to_message_id=update.message.message_id)
        elif "правил" in update.message.text:
            bot.send_message(chat_id=update.message.chat_id, text=random.choice(rules),
                             reply_to_message_id=update.message.message_id)

        else:
            bot.send_message(chat_id=update.message.chat_id, text=random.choice(reply_what_you_want),
                             reply_to_message_id=update.message.message_id)
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
