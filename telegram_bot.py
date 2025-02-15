import telebot
import os

TELEGRAM_TOKEN = os.getenv("8019649579:AAGe88yRXrwq53ZrFLU5Mm7g67gRy-rV8Yk")
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 أهلاً بك! هذا بوت تلقائي للنشر والردود.")

@bot.message_handler(commands=['post'])
def manual_post(message):
    bot.reply_to(message, "🚀 سيتم نشر المنشور قريبًا...")

print("🤖 بوت تيليجرام قيد التشغيل...")




bot.polling(none_stop=True)
