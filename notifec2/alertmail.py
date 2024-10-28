import psutil
import subprocess
import smtplib
from email.mime.text import MIMEText

NAMAEC2 = 'SERVER-DETINATIONCALCIO-PROD'
SENDER_EMAIL = 'ady.suryadi@comofootball.com'  
SENDER_PASSWORD = 'pebmvwhprhrrnbdt' 
RECEIVER_EMAILS = ['ady.suryadi@mola.tv', 'como.alerts@mola.tv']  # Tambahkan beberapa email

def send_email(subject, message, receiver_emails):
    try:
        # Setup MIME
        msg = MIMEText(message, 'plain')
        msg['From'] = SENDER_EMAIL
        msg['To'] = ", ".join(receiver_emails)
        msg['Subject'] = subject

        # SMTP setup
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_emails, msg.as_string())
        server.quit()

        print("Email sent successfully to multiple recipients!")
    except Exception as e:
        print(f"Error sending email: {e}")

def get_disk_usage_info():
    try:
        result = subprocess.run(['df', '-h'], stdout=subprocess.PIPE, text=True)
        return result.stdout
    except Exception as e:
        return f"Error retrieving disk usage info: {e}"

def check_disk_usage():
    disk = psutil.disk_usage('/')
    percent_used = disk.percent
    print(f"Disk usage: {percent_used}%")

    if percent_used >= 60:  # Sesuaikan threshold penggunaan disk
        subject = f'Alert {NAMAEC2}: Disk usage has reached {percent_used}%!'
        message = f'Disk usage on {NAMAEC2} has reached {percent_used}%.\n\n'
        disk_info = get_disk_usage_info()
        message += f'Disk Usage {NAMAEC2} Information:\n\n{disk_info}'
        send_email(subject, message, RECEIVER_EMAILS)

if __name__ == "__main__":
    check_disk_usage()
