import requests, sys, logging
import telebot
from telebot import types
#
#         Specifi logging object
#
log = logging.getLogger("WebRecon")



def send_tg(token, chat_id, updates: list):
    #  Defining the variables we need
    report_lines = []
    bot = telebot.TeleBot(token)

    if not updates:
        bot.send_message(chat_id, "No updates found", parse_mode='HTML')
        return

    # Defining message content
    for item in updates:
        if item['action'] == "insert":
            line = f"🆕 <b>NEW:</b> [{item['url']}] (Status: {item['status']})"
        else:
            line = f"🔄 <b>CHANGE:</b> [{item['url']}] ({item['stored_status']} -> {item['status']})"
        report_lines.append(line)      

    final_message = "\n\n".join(report_lines)
    # Sending message to Telegram bot chat
    try:
        bot.send_message(chat_id, final_message, parse_mode='HTML')
    except Exception as err:
        log.error(f"An error has occured: {err}. File: {__file__}")

    log.info(f"The report has been sent to the Telegram chat")    



