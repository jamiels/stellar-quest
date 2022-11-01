from stellar_sdk import *
from tools import *

server, base_fee = get_server()
toml_url = '0y7myfp83o88.runkit.sh/'

quest_kp = Keypair.from_secret('SAOZ7C6URXPDXPRQNJNENOKEULCKI7CNJTH5UHA3VS4AOZSDDV3S7H5O')
fund(quest_kp)

quest_ac = server.load_account(quest_kp)

txb = (get_txb(quest_ac)
        .append_set_options_op(
            home_domain=toml_url
        )      
)

tx = txb.build()
tx.sign(quest_kp)
display_tx_results(server.submit_transaction(tx))