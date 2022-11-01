from stellar_sdk import *
from tools import *

server, base_fee = get_server()
quest_kp = Keypair.from_secret('SDGUHAAPVKGWWZKUVNIGCRSQWRN2YKWX6QG4755LWNNEXCVO5WNDJSWK')
sponsor_kp = gen_keypair()

fund(sponsor_kp)

sponsor_ac = server.load_account(sponsor_kp)


txb = (get_txb(sponsor_ac)
    .append_begin_sponsoring_future_reserves_op(
        sponsored_id=quest_kp.public_key
    )
    .append_create_account_op(
        destination=quest_kp.public_key,
        starting_balance='0'
    )
    .append_end_sponsoring_future_reserves_op(        
        source=quest_kp.public_key
    )    
) 

tx = txb.build()
tx.sign(sponsor_kp)
tx.sign(quest_kp)
display_tx_results(server.submit_transaction(tx))
