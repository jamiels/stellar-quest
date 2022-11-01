from stellar_sdk import *
from tools import *

quest_kp = Keypair.from_secret('SATQ4LDEMDDVQMMJGETPKXBQNFOR54J3UL3L5TTSOUJDLJBTLCSTWIYZ')
new_kp = gen_keypair()
server, base_fee = get_server()
quest_ac = server.load_account(quest_kp)

tx = (get_txb(quest_ac)
        .append_create_account_op(
            destination=new_kp.public_key,
            starting_balance='1000'
    ).build())
tx.sign(quest_kp)
display_tx_results(server.submit_transaction(tx))

