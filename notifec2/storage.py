import psutil
import subprocess
import requests

# Konfigurasi Telegram Bot
TELEGRAM_BOT_TOKEN = '7234985493:AAGKYAAZCcY7yxmLSV6CF7e7Hz_QEjT2L5I'  # Ganti dengan token bot Telegram Anda
CHAT_ID = '-4508420593'              # Ganti dengan chat ID Anda
NAMAEC2 = 'SERVER-DESTINATIONCALCIO-PROD'

# Fungsi untuk mengirim pesan ke Telegram
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'HTML'  # Agar Telegram memformat pesan dengan HTML
    }
    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
        print("Message sent successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Error sending message: {e}")

# Fungsi untuk mendapatkan output df -h
def get_disk_usage_info():
    try:
        # Menjalankan perintah df -h dan mendapatkan outputnya
        result = subprocess.run(['df', '-h'], stdout=subprocess.PIPE, text=True)
        return result.stdout
    except Exception as e:
        return f"Error retrieving disk usage info: {e}"

# Fungsi untuk memeriksa penggunaan disk
def check_disk_usage():
    # Memeriksa penggunaan disk
    disk = psutil.disk_usage('/')
    percent_used = disk.percent
    print(f"Disk usage: {percent_used}%")

    # Kirim pesan ke Telegram jika penggunaan disk >= 60%
    if percent_used >= 6:
        message = f'Alert {NAMAEC2}: Disk usage has reached {percent_used}%!\n\n'
        message += f'Disk Usage {NAMAEC2} Information:\n'
        message += '<pre>' + get_disk_usage_info() + '</pre>'
        send_telegram_message(message)

if __name__ == "__main__":
    check_disk_usage()
