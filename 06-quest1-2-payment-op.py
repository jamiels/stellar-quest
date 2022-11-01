from stellar_sdk import *
from tools import *

quest_kp = Keypair.from_secret('SCOLO6W7TBF5UUWQFG3YMYXL6R57EARDR6IRMDBES5ALDANLGOTXIKIQ')
destination_kp = gen_keypair()
fund(quest_kp,destination_kp)

server, base_fee = get_server()
quest_ac = server.load_account(quest_kp)

tx = (get_txb(quest_ac)
        .append_payment_op(
            destination=destination_kp.public_key,
            asset=Asset.native(),
            amount='100'
    ).build())

display_tx_results(
    server.submit_transaction(
        tx.sign(quest_kp)
))


