import asyncio
import aiohttp
import os
import json
from dotenv import load_dotenv
from datetime import datetime, timezone

# Load environment variables from .env file
load_dotenv()

async def fetch_balance(session, chain_id, address, api_key):
    url = "https://api.etherscan.io/v2/api"
    params = {
        "chainid": chain_id,
        "module": "account",
        "action": "balance",
        "address": address,
        "tag": "latest",
        "apikey": api_key
    }
    
    async with session.get(url, params=params) as response:
        data = await response.json()
        return {
            'balance': data['result'],
            'timestamp': data.get('timestamp', str(int(datetime.now(timezone.utc).timestamp())))
        }

def save_to_json(data):
    filename = f"balance_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Data saved to {filename}")

async def main():
    # Retrieve API key from environment variable
    api_key = os.getenv('ETHERSCAN_API_KEY')
    
    if not api_key:
        print("Error: ETHERSCAN_API_KEY not found in environment variables.")
        return

    # Get user input for chain IDs and address
    chains_input = input("Enter chain IDs (comma-separated, e.g., 42161,8453,10): ")
    chains = [int(chain.strip()) for chain in chains_input.split(',')]
    
    address = input("Enter the Ethereum address to check: ")

    results = []

    async with aiohttp.ClientSession() as session:
        for chain in chains:
            result = await fetch_balance(session, chain, address, api_key)
            balance_eth = int(result['balance']) / 1e18  # Convert Wei to ETH
            print(f"Chain ID {chain}: Balance = {balance_eth:.18f} ETH")
            
            results.append({
                'chain_id': chain,
                'address': address,
                'balance_wei': result['balance'],
                'balance_eth': f"{balance_eth:.18f}",
                'timestamp': result['timestamp'],
                'utc_time': datetime.fromtimestamp(int(result['timestamp']), timezone.utc).isoformat()
            })

    # Save results to JSON file
    save_to_json(results)

if __name__ == "__main__":
    asyncio.run(main())
