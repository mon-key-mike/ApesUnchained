import requests

url = "https://api-mainnet.magiceden.dev/v3/rtp/ethereum/cross-posting-orders/v1?limit=50"

headers = {
    "accept": "*/*",
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)

print(response.text)
