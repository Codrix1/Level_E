

from cryptography.hazmat.primitives.ciphers import Cipher , algorithms , modes
from cryptography.hazmat.primitives import padding
import rsa , os


def get_rsa_key():
    with open("encryption\\public.pem","rb") as file:
        public_key = rsa.PublicKey.load_pkcs1(file.read())
    return public_key 


def rsa_encrypt(msg):
    key = get_rsa_key()
    encrypted = rsa.encrypt(msg , key )
    print("this is the encrypted message: "+str(encrypted) +"\n")
    return encrypted

def aes_encrypt(data:str , key:bytes ) -> bytes:
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data)+ padder.finalize()
    encryptor = Cipher(algorithms.AES(key) , modes.ECB()).encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return ciphertext 

def load_msg():
    with open ("large_message.txt" , "rb") as file:
        msg = file.read()
    key = os.urandom(16)
    encrypted_msg = aes_encrypt(msg , key)
    encrypted_key = rsa_encrypt(key)

    