
from dotenv import load_dotenv

import telebot
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")

# طباعة التوكن للتأكد أنه يتم تحميله
print(f"🔍 `TOKEN` بعد التحميل: {TOKEN}")


# قراءة التوكن من متغيرات البيئة
TELEGRAM_TOKEN = os.getenv("TOKEN")  

if not TELEGRAM_TOKEN:
    print(f"🔍 قيمة `TOKEN` المسترجعة: {os.getenv('TOKEN')}")
    print("🚨 خطأ: لم يتم العثور على توكن تيليجرام! تأكد من إضافته في متغيرات البيئة في Railway.")
    print("🔍 تحقق: قائمة متغيرات البيئة المتاحة:")
    print(os.environ)  # طباعة جميع المتغيرات البيئية لمعرفة إن كان `TOKEN` موجودًا
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
