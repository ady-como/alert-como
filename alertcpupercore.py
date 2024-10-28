import psutil
import requests
import time

slack_webhook_url = "https://hooks.slack.com/services/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"
threshold = 80

def send_slack_message(text):
    payload = {'text': text}
    r = requests.post(slack_webhook_url, json=payload)
    return r

while True:
    # Mengecek penggunaan CPU per core
    cpu_per_core = psutil.cpu_percent(interval=1, percpu=True)
    
    for i, usage in enumerate(cpu_per_core):
        if usage > threshold:
            message = f"CPU Core {i} DC-Prod: {usage}%"
            send_slack_message(message)
    
    time.sleep(1)
