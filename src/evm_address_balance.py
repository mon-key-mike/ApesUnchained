import asyncio
import aiohttp

async def fetch_balance(session, chain_id, address, api_key):
    url = f"https://api.etherscan.io/v2/api"
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
        return data['result']

async def main():
    # Replace 'YourApiKeyToken' with your actual Etherscan API key
    api_key = "YourApiKeyToken"
    
    # Address to check balance for
    address = "0xb5d85cbf7cb3ee0d56b3bb207d5fc4b82f43f511"
    
    # Chain IDs for Arbitrum, Base, and Optimism
    chains = [42161, 8453, 10]

    async with aiohttp.ClientSession() as session:
        for chain in chains:
            balance = await fetch_balance(session, chain, address, api_key)
            print(f"Chain ID {chain}: Balance = {balance}")

if __name__ == "__main__":
    asyncio.run(main())
