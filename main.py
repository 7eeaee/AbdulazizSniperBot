
import os
import requests
import datetime
import time
import pytz
from telegram import Bot

# إعداد المتغيرات
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")  # مخصص لاحقاً بعد معرفة رقم المستخدم
bot = Bot(token=TOKEN)

def get_stock_recommendation():
    # نموذج توصية ثابت مؤقتاً (لاحقاً يمكن ربط API حقيقي للأسهم)
    return '''
📊 توصية اليوم - AbdulazizSniperBot

🎯 السهم: $ZENA
📈 Pre-Market: +28.6%
📊 حجم تداول: 9.1 مليون
📰 الخبر: FDA approval for new diabetes treatment
📉 RSI: 61 (مثالي للصعود)

✅ التوصية:
ادخل مع افتتاح السوق (4:30م بتوقيت السعودية)
🎯 الهدف: +20% إلى +35%
🛑 وقف الخسارة: -6%
'''

def wait_until_4_25():
    tz = pytz.timezone('Asia/Riyadh')
    while True:
        now = datetime.datetime.now(tz)
        if now.hour == 16 and now.minute == 25:
            return
        time.sleep(30)

if __name__ == "__main__":
    while True:
        wait_until_4_25()
        message = get_stock_recommendation()
        bot.send_message(chat_id=CHAT_ID, text=message)
        time.sleep(60)  # منع التكرار خلال الدقيقة
