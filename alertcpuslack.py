import psutil
import requests
import time

slack_webhook_url = "https://hooks.slack.com/services/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"
threshold = 65

def send_slack_message(text):
    payload = {'text': text}
    r = requests.post(slack_webhook_url, json=payload)
    return r

while True:
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > threshold:
        message = f"CPU DC-Prod: {cpu_usage}%"
        send_slack_message(message)
    time.sleep(1)
