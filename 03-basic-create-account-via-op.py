from stellar_sdk import Keypair, Server, Network, TransactionBuilder

source_keypair = Keypair.random()

print('source keypair:')
print(source_keypair.public_key) # public key
print(source_keypair.secret) # private key aka secret key aka secret
input('hit enter to continue')

target_keypair = Keypair.random()
print('target key pair')
print(target_keypair.public_key) # public key
print(target_keypair.secret) # private key aka secret key aka secret
input('hit enter to continue')

print('funding source account')
resp = requests.get(f'https://friendbot.stellar.org?addr={source_keypair.public_key}')
print(resp.content)
input('hit enter to continue')

server = Server("https://horizon-testnet.stellar.org")

source_account = server.load_account(source_keypair.public_key)
base_fee = server.fetch_base_fee() # 100
print('base fee',base_fee)

print('building the transaction')
txb = TransactionBuilder(
        source_account=source_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=base_fee   )

txb.append_create_account_op(target_keypair.public_key,"1")

print('transaction is built')
tx = txb.build()

print('the sender is signing the transaction')
tx.sign(source_keypair.secret)
print('submitting transaction to horizon')
server.submit_transaction(tx)







# account = server.accounts().account_id(keypair.public_key).call()
# #print(account)
# for b in account['balances']:
#     print(b['balance'])
 
