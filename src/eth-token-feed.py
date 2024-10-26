import requests

url = "https://api-mainnet.magiceden.dev/v3/rtp/ethereum/tokens/token/activity/v5?limit=20&sortBy=eventTimestamp&includeMetadata=true"

headers = {
    "accept": "*/*",
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)

print(response.text)
