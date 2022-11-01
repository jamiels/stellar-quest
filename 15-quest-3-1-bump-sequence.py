from stellar_sdk import *
from tools import *

server, base_fee = get_server()
quest_kp = Keypair.from_secret('SC6DZ2NMWS4AW74VCHV425SDLSDSAGC3DKBPQ6RJA3GVXKEXGBZB3QPB')


fund(quest_kp)

quest_ac = server.load_account(quest_kp)
print(f'Current sequence number {quest_ac.sequence}')

txb = (get_txb(quest_ac)
    .append_bump_sequence_op(bump_to=quest_ac.sequence + 100)       
) 
            
tx = txb.build()
tx.sign(quest_kp)
display_tx_results(server.submit_transaction(tx))
print(f'Current sequence number {quest_ac.sequence}')


bumped_ac = Account(quest_kp.public_key,quest_ac.sequence+99)
txb = (get_txb(bumped_ac)
        .append_manage_data_op(
            data_name='sequence',
            data_value='bumped'
        )
      
)
tx = txb.build()
tx.sign(quest_kp)
display_tx_results(server.submit_transaction(tx))
print(f'Current sequence number {quest_ac.sequence}')
quest_ac = server.load_account(quest_kp)
print(f'Current sequence number {quest_ac.sequence}')