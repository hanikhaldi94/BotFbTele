import telebot
import os

TELEGRAM_TOKEN = os.getenv("TOKEN")

if not TELEGRAM_TOKEN:
    print("🚨 خطأ: لم يتم العثور على توكن تيليجرام! تأكد من إضافته في متغيرات البيئة في Railway.")
    exit(1)  # إنهاء البرنامج إذا لم يتم العثور على التوكن


bot = telebot.TeleBot(TELEGRAM_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 أهلاً بك! هذا بوت تلقائي للنشر والردود.")

@bot.message_handler(commands=['post'])
def manual_post(message):
    bot.reply_to(message, "🚀 سيتم نشر المنشور قريبًا...")

print("🤖 بوت تيليجرام قيد التشغيل...")




bot.polling(none_stop=True)
