from stellar_sdk import *
from tools import *

quest_kp = Keypair.from_secret('SC5KPJLBAQVBYIZ56X72TAZAUUX6NTQECGEG3I5QK7FT3AYZTBNAIA2G')
issuer_kp = gen_keypair()
fund(quest_kp,issuer_kp)

server, base_fee = get_server()
quest_ac = server.load_account(quest_kp)
issuer_ac = server.load_account(issuer_kp)
asset = Asset(code='INSTA',issuer=issuer_kp.public_key)


tx = (get_txb(quest_ac)
        .append_change_trust_op(
            asset=asset,
            limit="100",
            source=quest_kp.public_key # this is WHO is trust the issuer
    ).build())

tx.sign(quest_kp)
display_tx_results(server.submit_transaction(tx))

# mint asset
tx = (get_txb(issuer_ac)
        .append_payment_op(
            destination=quest_kp.public_key,
            asset=asset,
            amount='1'
    ).build())

tx.sign(issuer_kp)
display_tx_results(server.submit_transaction(tx))
