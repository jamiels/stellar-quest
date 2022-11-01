from stellar_sdk import *
from tools import *

server, base_fee = get_server()
quest_kp = Keypair.from_secret('SDZSOH4NQSIIRM2VIXI2EEQDLUYTFJZQRERNY7M3MB7XTVTNB2XZVEEE')
second_kp = Keypair.from_secret('SA35SOIZ4VHWJDH2RHRUKWX3KZRE35IO2KFF5Z77ZJI7I2GZDK6WNYEM')
third_kp = Keypair.from_secret('SA57DCKWO3LYE537A5PR244H3B7PU5CLAFQSP26SOCCQGPFXMGHBD4SJ')
# second_kp = gen_keypair() -- Note that once you generate keypair and the below transaction is successful, the keypair will be needed for any future updates to the quest account because the transaction setups a multisig
# third_kp = gen_keypair()

fund(quest_kp)

quest_ac = server.load_account(quest_kp)

tx = (get_txb(quest_ac)
        .append_set_options_op(
            master_weight=1,
            low_threshold=5,
            med_threshold=5,
            high_threshold=5
        )
        .append_set_options_op(
            signer=Signer(
                SignerKey(second_kp.raw_public_key(),SignerKeyType.SIGNER_KEY_TYPE_ED25519), weight=2)
        )
        .append_set_options_op(
            signer=Signer(
                SignerKey(third_kp.raw_public_key(),SignerKeyType.SIGNER_KEY_TYPE_ED25519), weight=2)
        )              
).build()
            
tx.sign(quest_kp)
tx.sign(second_kp)
tx.sign(third_kp)
display_tx_results(server.submit_transaction(tx))