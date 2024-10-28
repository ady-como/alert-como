import psutil
import requests
import time


#TELEGRAM_BOT_TOKEN = '7234985493:AAGKYAAZCcY7yxmLSV6CF7e7Hz_QEjT2L5I'  # Ganti dengan token bot Telegram Anda
#CHAT_ID = '-4508420593' 

bot_token = "7234985493:AAGKYAAZCcY7yxmLSV6CF7e7Hz_QEjT2L5I"
chat_id = "-4508420593"
threshold = 75

def send_telegram_message(text):
  url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
  payload = {'chat_id': chat_id, 'text': text}
  r = requests.post(url, data=payload)
  return r

while True:
  cpu_usage = psutil.cpu_percent(interval=1)
  if cpu_usage > threshold:
    message = f"Peringatan! Penggunaan CPU DC saat ini: {cpu_usage}%"
    send_telegram_message(message)
  time.sleep(1)
