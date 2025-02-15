import os
import time
import telebot
import traceback
from dotenv import load_dotenv

# تحميل متغيرات البيئة
load_dotenv()
TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("❌ لم يتم العثور على التوكن! تأكد من ضبط متغيرات البيئة.")

bot = telebot.TeleBot(TOKEN)

# أمر البدء
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 أهلاً بك! كيف يمكنني مساعدتك؟")

# أمر المساعدة
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "📌 قائمة الأوامر المتاحة:\n/start - بدء البوت\n/help - المساعدة\n/info - معلومات عن البوت")

# أمر المعلومات
@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message, "🤖 هذا بوت تجريبي لمساعدتك في الأتمتة!")

# الاستجابة لأي رسالة أخرى
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"📩 لقد أرسلت: {message.text}")

print("🤖 بوت تيليجرام قيد التشغيل...")

def main():
    while True:
        try:
            bot.polling(none_stop=True, interval=1)
        except Exception as e:
            print(f"⚠️ خطأ: {e}\n{traceback.format_exc()}")
            print("🔄 إعادة تشغيل البوت بعد 5 ثوانٍ...")
            time.sleep(5)

if __name__ == "__main__":
    main()
