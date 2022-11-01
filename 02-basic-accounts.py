from stellar_sdk import Keypair, Server
import requests

kp = Keypair.random()

print(kp.public_key)
print(kp.secret)

# get funds from friendbot faucet
resp = requests.get(f'https://friendbot.stellar.org?addr={kp.public_key}')
server = Server("https://horizon-testnet.stellar.org")

# returns a dictionary
account = server.accounts().account_id(kp.public_key).call()
#print(account)
for b in account['balances']:
    print(b['balance'])

# returns Account object
account = server.load_account(kp.public_key)
 
