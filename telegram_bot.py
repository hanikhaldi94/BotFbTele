import os
import time
import telebot
import logging
from dotenv import load_dotenv
from flask import Flask, request

# تحميل متغيرات البيئة
load_dotenv()
TOKEN = os.getenv("TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # رابط السيرفر لاستقبال التحديثات

if not TOKEN:
    raise ValueError("❌ لم يتم العثور على التوكن! تأكد من ضبط متغيرات البيئة.")

bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

# إعداد سجل الأخطاء
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# إعداد Webhook
@server.route(f'/{TOKEN}', methods=['POST'])
def receive_update():
    json_update = request.get_json()
    bot.process_new_updates([telebot.types.Update.de_json(json_update)])
    return "", 200

# تعيين Webhook عند بدء التشغيل
@server.before_first_request
def setup_webhook():
    bot.remove_webhook()
    time.sleep(1)
    bot.set_webhook(url=f"{WEBHOOK_URL}/{TOKEN}")
    logger.info("✅ Webhook تم تفعيله بنجاح!")

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

# الرد الذكي على الرسائل
@bot.message_handler(func=lambda message: True)
def smart_reply(message):
    text = message.text.lower()
    if "مرحبا" in text or "اهلا" in text:
        bot.reply_to(message, "✨ مرحباً بك! كيف يمكنني مساعدتك؟")
    elif "كيف حالك" in text:
        bot.reply_to(message, "😊 أنا بخير، شكراً لسؤالك!")
    else:
        bot.reply_to(message, f"📩 لقد أرسلت: {message.text}")

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
