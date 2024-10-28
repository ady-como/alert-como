import psutil
import subprocess
import requests
import json

SLACK_WEBHOOK_URL = 'https://hooks.slack.com/services/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'  
NAMAEC2 = 'SERVER-DESTINATIONCALCIO-PROD'

def send_slack_message(message):
    payload = {
        'text': message
    }
    try:
        response = requests.post(
            SLACK_WEBHOOK_URL, 
            data=json.dumps(payload),
            headers={'Content-Type': 'application/json'}
        )
        response.raise_for_status()
        print("Message sent successfully to Slack!")
    except requests.exceptions.RequestException as e:
        print(f"Error sending message to Slack: {e}")


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

    if percent_used >= 60:
        message = f'Alert {NAMAEC2}: Disk usage has reached {percent_used}%!\n\n'
        message += f'Disk Usage {NAMAEC2} Information:\n'
        message += '```' + get_disk_usage_info() + '```'  
        send_slack_message(message)

if __name__ == "__main__":
    check_disk_usage()
