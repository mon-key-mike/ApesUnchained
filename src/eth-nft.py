import requests

url = "https://api-mainnet.magiceden.dev/v3/rtp/ethereum/collections/v7?includeMintStages=false&includeSecurityConfigs=false&normalizeRoyalties=false&useNonFlaggedFloorAsk=false&sortBy=allTimeVolume&limit=20"

headers = {
    "accept": "*/*",
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)

print(response.text)
