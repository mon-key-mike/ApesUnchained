import requests
import json

# Replace with your actual Discord webhook URL
WEBHOOK_URL = "https://your-bridge-server.herokuapp.com/webhook"

payload = {
    "content": "New Ape Discovery\nScientists have observed apes using smartphones in the wild!",
    "author": {
        "username": "monkeymike"
    },
    "timestamp": "2023-05-15T12:00:00.000Z"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(WEBHOOK_URL, data=json.dumps(payload), headers=headers)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")
