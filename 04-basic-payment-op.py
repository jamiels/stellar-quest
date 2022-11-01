from stellar_sdk import *
from tools import *

source_kp = gen_keypair()
target_kp = gen_keypair()
fund(source_kp)
server, base_fee = get_server_testnet()

source_account = server.load_account(source_kp.public_key)

print('Building tx')
txb = (
        TransactionBuilder(
        source_account=source_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=base_fee)
        .append_create_account_op(target_kp.public_key,"1")
        .append_payment_op(destination=target_kp.public_key,
                    asset=Asset.native(),
                    amount="1000")
        .add_text_memo('safiyahs gift')
        .set_timeout(30)
        )

tx = txb.build()
tx.sign(source_kp.secret)
tx_result = server.submit_transaction(tx)
print_tx_results(tx_result)







# account = server.accounts().account_id(keypair.public_key).call()
# #print(account)
# for b in account['balances']:
#     print(b['balance'])
 
