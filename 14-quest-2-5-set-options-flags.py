from stellar_sdk import *
from tools import *

server, base_fee = get_server()
quest_kp = Keypair.from_secret('SAVUF3LGRKU3E2RCVS3464ZTP2PJ7HOLZS2QZQPIWPRLVE7B4Q5FPSPZ')
issuer_kp = gen_keypair()

fund(quest_kp,issuer_kp)

quest_ac = server.load_account(quest_kp)
issuer_ac = server.load_account(issuer_kp)

asset = Asset(code='CONTROL',issuer=issuer_kp.public_key)


txb = (get_txb(issuer_ac)
        .append_set_options_op(
            set_flags=3
        )
        .append_change_trust_op(
            asset=asset,
            source=quest_kp.public_key
        )
        .append_set_trust_line_flags_op(
            trustor=quest_kp.public_key,
            asset=asset,
            set_flags=TrustLineFlags(TrustLineFlags.AUTHORIZED_FLAG),
            source=issuer_kp.public_key
        )
        .append_payment_op(
            destination=quest_kp.public_key,
            asset=asset,
            amount='100'
        )
        .append_set_trust_line_flags_op(
            trustor=quest_kp.public_key,
            asset=asset,
            clear_flags=TrustLineFlags(TrustLineFlags.AUTHORIZED_FLAG),
            source=issuer_kp.public_key
        )         
) 
            
tx = txb.build()
tx.sign(quest_kp)
tx.sign(issuer_kp)

display_tx_results(server.submit_transaction(tx))