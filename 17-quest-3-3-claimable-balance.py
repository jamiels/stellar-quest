from stellar_sdk import *
from tools import *

server, base_fee = get_server()
quest_kp = Keypair.from_secret('SAPOVNTT2AEELNHN2HTSVH3UUR3MOYNN2RZ6SFUCQDEO7H5HEOP52JMX')
claimant_kp = gen_keypair()

fund(quest_kp, claimant_kp)

quest_ac = server.load_account(quest_kp)

claimant = Claimant(claimant_kp.public_key,
                ClaimPredicate.predicate_not(
                    ClaimPredicate.predicate_before_relative_time(seconds=3)))

questReclaimant = Claimant(quest_kp.public_key,ClaimPredicate.predicate_unconditional()) # reclaim whenever

tx = (get_txb(quest_ac)
        .append_create_claimable_balance_op (
            asset=Asset.native(),
            amount='100',
            claimants=[claimant,questReclaimant]
        )   
    ).build()

tx.sign(quest_kp)
tx_result = server.submit_transaction(tx)
display_tx_results(tx_result)

# Make claim
res = server.claimable_balances().for_claimant(claimant_kp.public_key).limit(1).call()
claimable_balance_id = res['_embedded']['records'][0]['id']
print('claimable bal id',claimable_balance_id)
input('pause...') # let 3 seconds elapse
claimant_ac = server.load_account(claimant_kp)
tx = (get_txb(claimant_ac)
        .append_claim_claimable_balance_op (
            balance_id=claimable_balance_id
        )   
    ).build() 

tx.sign(claimant_kp)
display_tx_results(server.submit_transaction(tx))
