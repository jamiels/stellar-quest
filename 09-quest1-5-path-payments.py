from readline import append_history_file
from stellar_sdk import *
from tools import *

server, base_fee = get_server()

quest_kp = Keypair.from_secret('SAXDK64FHUOIVKX5IF7H3POI6WZLGE62UVUXBEGQRG2V6HMOEOVVPE4Z')
issuer_kp = gen_keypair()
distributor_kp = gen_keypair()
destination_kp = gen_keypair()

fund(quest_kp,issuer_kp,distributor_kp,destination_kp)


quest_ac = server.load_account(quest_kp)
issuer_ac = server.load_account(issuer_kp)
distributor_ac = server.load_account(distributor_kp)
destination_ac = server.load_account(destination_kp)

asset = Asset(code='PATH',issuer=issuer_kp.public_key)



txb = (get_txb(quest_ac)
        .append_change_trust_op(
                asset=asset,
                source=destination_kp.public_key)
        .append_change_trust_op(
                asset=asset,
                source=distributor_kp.public_key)
        .append_payment_op(
                destination=distributor_kp.public_key,
                asset=asset,
                amount='1000000',
                source=issuer_kp.public_key)
        .append_create_passive_sell_offer_op(
            selling=asset,
            buying=Asset.native(),
            amount='2000',
            price='1',
            source=distributor_kp.public_key)
        .append_create_passive_sell_offer_op(
            selling=Asset.native(),
            buying=asset,
            amount='2000',
            price='1',
            source=distributor_kp.public_key)
        .append_path_payment_strict_send_op(
            send_asset=Asset.native(),
            send_amount='1000',
            destination=destination_kp.public_key,
            dest_asset=asset,
            dest_min='1000',
            path=[asset,Asset.native()])
        .append_path_payment_strict_receive_op(
            send_asset=asset,
            send_max='450',
            destination=quest_kp.public_key,
            dest_asset=Asset.native(),
            dest_amount='450',
            source=destination_kp.public_key,
            path=[asset,Asset.native()]))

tx = txb.build()

tx.sign(quest_kp)
tx.sign(issuer_kp)
tx.sign(distributor_kp)
tx.sign(destination_kp)

display_tx_results(server.submit_transaction(tx))

