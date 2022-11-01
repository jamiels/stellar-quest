# https://developers.stellar.org/docs/tutorials/create-account
# pip install stellar-sdk

from stellar_sdk import Keypair

kp = Keypair.random()

print(kp.public_key) 
print(kp.secret) 

kp = Keypair.from_secret(kp.secret)
print(kp.public_key) 
print(kp.secret) 



 
