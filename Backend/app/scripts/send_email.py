import requests
import time
import random

URL = "http://localhost:8000/api/email/incoming"

emails = [
    "Hi, we are also considering Salesforce for this.",
    "Your pricing seems a bit high compared to others.",
    "We might not continue with this solution.",
    "Can you share more details?",
]

senders = [
    "shivamrajpoot4318@gmail.com",
    "shivamrajput9827998@gmail.com",
    "999shivamlodhi@gmail.com"
]

while True:
    payload = {
        "email": random.choice(emails),
        "sender": random.choice(senders)
    }

    response = requests.post(URL, json=payload)

    print("Sent:", payload)
    print("Response:", response.json())

    time.sleep(5)  # every 5 sec new email