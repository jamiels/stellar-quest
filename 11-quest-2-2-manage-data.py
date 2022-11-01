from stellar_sdk import *
from tools import *

server, base_fee = get_server()

quest_kp = Keypair.from_secret('SCHJ3IKLUDZQTXFNE5H5CUHAIQ6ITVYFRCGNGFIHR7BQCYIOLNOYROUC')
destination_kp = gen_keypair()

fund(quest_kp,destination_kp)

quest_ac = server.load_account(quest_kp)

txb = (get_txb(quest_ac)
        .append_manage_data_op(
            data_name='Hello',
            data_value='World'
        )
        .append_manage_data_op(
            data_name='Hello',
            data_value='Instamint!'
        )        
)

tx = txb.build()
tx.sign(quest_kp)
display_tx_results(server.submit_transaction(tx))