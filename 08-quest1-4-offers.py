from stellar_sdk import *
from tools import *

quest_kp = Keypair.from_secret('SCBXBVAWYGEVYWZOTJFJ2LX3GU2D5346J42XHDBWBWIMKGZMFRYTMY43')
server, base_fee = get_server()
quest_ac = server.load_account(quest_kp)
usdc = Asset(code='USDC',issuer='GBBD47IF6LWK7P7MDEVSCWR7DPUWV3NY3DTQEVFL4NAT4AQH3ZLLFLA5')

tx = (get_txb(quest_ac)
        .append_change_trust_op(
            asset=usdc)
        .append_manage_buy_offer_op(
            selling=Asset.native(),
            buying=usdc,
            amount='100',
            price='10',
            offer_id=0,
            source=quest_kp.public_key)
        .append_manage_sell_offer_op(
            selling=Asset.native(),
            buying=usdc,
            amount='1000',
            price='.1',
            offer_id=0,
            source=quest_kp.public_key            
        )
        .append_create_passive_sell_offer_op(
            selling=Asset.native(),
            buying=usdc,
            amount='1000',
            price='.1',
            source=quest_kp.public_key            
        )
        .build())


tx.sign(quest_kp)
display_tx_results(server.submit_transaction(tx))

