import asyncio
from eth_account import Account
from eth_account.messages import encode_defunct
from web3 import Web3

class Provider:
    async def request(self, params):
        # This is a mock implementation
        if params['method'] == "personal_sign":
            # In a real scenario, this would interact with an actual Ethereum wallet
            # Here, we're using eth_account to simulate the signing process
            message = params['params'][0]
            address = params['params'][1]
            password = params['params'][2]  # Note: typically, password isn't used in personal_sign

            # Create a local account for demonstration (in real use, this would be the user's account)
            acct = Account.create()

            # Sign the message
            signed_message = Account.sign_message(encode_defunct(hexstr=message), acct.key)
            
            return signed_message.signature.hex()
        else:
            raise Exception("Unsupported method")

async def sign_message(provider, address):
    message = "Hello, World! 🌍 Welcome to the Magic Eden wallet on Ethereum"

    # Convert the message to hexadecimal
    # In Python, we can use the bytes.fromhex() method instead of Array.from()
    msg = "0x" + message.encode().hex()

    try:
        sign = await provider.request({
            "method": "personal_sign",
            "params": [msg, address, "Example password"]
        })
        print(f"Signed message: {sign}")
        return sign
    except Exception as err:
        print(f"An error occurred: {err}")
        return None

# Example usage
async def main():
    provider = Provider()  # Create a mock provider
    address = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"  # Example Ethereum address
    await sign_message(provider, address)

# Run the async function
asyncio.run(main())
