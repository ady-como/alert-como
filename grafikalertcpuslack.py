import psutil
import requests
import time
import matplotlib.pyplot as plt
from collections import deque


slack_webhook_url = "https://hooks.slack.com/services/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"
threshold = 2


def send_slack_message(text):
    payload = {'text': text}
    r = requests.post(slack_webhook_url, json=payload)
    return r


cpu_history = deque([0]*60, maxlen=60)  
plt.ion()  
fig, ax = plt.subplots()
line, = ax.plot(cpu_history)
ax.set_ylim(0, 100)
ax.set_xlabel('Time (seconds)')
ax.set_ylabel('CPU Usage (%)')
ax.set_title('Real-time CPU Usage')


while True:
    
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_history.append(cpu_usage)


    line.set_ydata(cpu_history)
    ax.relim()
    ax.autoscale_view()
    plt.draw()
    plt.pause(0.1)


    if cpu_usage > threshold:
        message = f"CPU DC-Prod: {cpu_usage}%"
        send_slack_message(message)

   
    time.sleep(1)
