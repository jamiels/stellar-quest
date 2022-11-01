from stellar_sdk import *
from dotenv import load_dotenv
import os, requests

testnet = Server('https://horizon-testnet.stellar.org')
mainnet = Server('https://horizon.stellar.org')
base_fee = testnet.fetch_base_fee()
base_fee_mainnet = mainnet.fetch_base_fee()

load_dotenv()

def get_txb(source_account):
    txb = TransactionBuilder(
        source_account=source_account,
        base_fee=base_fee,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE).set_timeout(30)
    return txb

def get_server():
    return testnet, base_fee

def get_base_fee():
    return base_fee

def get_base_fee_mainnet():
    return base_fee_mainnet

def get_server_mainnet():
    base_fee = mainnet.fetch_base_fee()
    return mainnet, base_fee_mainnet

def get_wallet():
    wallet_secret = os.getenv('wallet_secret')
    wallet_keypair = Keypair.from_secret(wallet_secret)
    return wallet_keypair

def fund(*argv):
    resps = []
    for addr in argv:
        print(f'Funding {addr.public_key}')
        resp = requests.get(f'https://friendbot.stellar.org?addr={addr.public_key}')
        if resp.status_code!=200:
            print(resp.content)
        resps.append(resp)
    return resps

def gen_keypair():
    kp = Keypair.random()
    print(f'Public key: {kp.public_key}') # public key aka verifying key
    print(f'Secret key: {kp.secret}') # private key aka secret key aka secret aka signing key
    return kp

def display_account_info(acc):
    print(acc)

def display_tx_results(tx):
    print('---- Transaction Results')
    print('Tx ID: ',tx['id'])
    print('Successful: ', tx['successful'])
    print('URL: ',tx['_links']['transaction']['href'])
    print('Ops: ',tx['operation_count'])
    print('----')
