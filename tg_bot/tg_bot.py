# TELEGRAM BOT
from translate import to_cyrillic, to_latin
import telebot

TOKEN = '5658694572:AAGtq1Gp0z_YBCNP7vGWiusPUmE_uVxLtFo'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    answer = "Assalomu alaykum, Xush kelibsiz!"
    answer +=  "\nMatn kiriting:"
    bot.reply_to(message=message, text=answer)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    answer = lambda msg: to_cyrillic(msg) if msg.isaascii() else to_latin(msg)
    bot.reply_to(message, answer(msg))

bot.polling()
