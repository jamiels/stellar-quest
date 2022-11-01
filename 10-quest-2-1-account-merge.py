from stellar_sdk import *
from tools import *

server, base_fee = get_server()

quest_kp = Keypair.from_secret('SCKIVMPAL2M3VDA2P6BUEC42I2UJGFOMGRA7FBLCMGEGOBXUGMH33E42')
destination_kp = gen_keypair()

fund(quest_kp,destination_kp)

quest_ac = server.load_account(quest_kp)

txb = (get_txb(quest_ac)
        .append_account_merge_op(
            destination=destination_kp.public_key
        )
)

tx = txb.build()
tx.sign(quest_kp)
display_tx_results(server.submit_transaction(tx))