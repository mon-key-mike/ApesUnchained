import requests

url = "https://api-mainnet.magiceden.dev/v3/rtp/ethereum/collections/trending/v1?period=1d&limit=50&sortBy=sales&normalizeRoyalties=false&useNonFlaggedFloorAsk=false"

headers = {
    "accept": "*/*",
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)

print(response.text)
