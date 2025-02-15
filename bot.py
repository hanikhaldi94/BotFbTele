# -*- coding: utf-8 -*-

import telebot

# ضع التوكن الجديد هنا
TOKEN = "8019649579:AAGe88yRXrwq53ZrFLU5Mm7g67gRy-rV8Yk"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "👋 أهلاً بك! هذا بوت تلقائي للنشر والردود.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"لقد قلت: {message.text}")

print("✅ البوت يعمل الآن...")
bot.polling()




