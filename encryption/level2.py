
from doctest import testfile
from hashlib import algorithms_available
import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from itsdangerous import NoneAlgorithm

def ans_1():
    data = b"secret"
    key = get_random_bytes(16)

    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(data, AES.block_size))

    iv_b64 = b64encode(cipher.iv).decode()
    ct_b64 = b64encode(ciphertext).decode()

    print("Encrypted:")
    print("IV:", iv_b64)
    print("Ciphertext:", ct_b64)


    iv = b64decode(iv_b64)
    ct = b64decode(ct_b64)

    cipher2 = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher2.decrypt(ct), AES.block_size)

    print("\nDecrypted:")
    print(plaintext.decode())

def ans_2():
    data = b"secret"
    key = get_random_bytes(16)

    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(data, AES.block_size))

    ct_b64 = b64encode(ciphertext).decode()

    print("Encrypted:")
    print("Ciphertext:", ct_b64)

    ct = b64decode(ct_b64)

    cipher2 = AES.new(key, AES.MODE_ECB)
    plaintext = unpad(cipher2.decrypt(ct), AES.block_size)

    print("\nDecrypted:")
    print(plaintext.decode())

import os
def ans_3():
    key = os.urandom(16)
    return key

from cryptography.hazmat.primitives.ciphers import Cipher , algorithms , modes
from cryptography.hazmat.primitives import padding

def encrypt(data:str , key:bytes , mode_cbc:bool)->tuple[bytes, bytes | None]:
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data)+ padder.finalize()
    
    if mode_cbc:
        iv = os.urandom(16)
        encryptor = Cipher(algorithms.AES(key) , modes.CBC(iv)).encryptor()
    else:
        iv = None
        encryptor = Cipher(algorithms.AES(key) , modes.ECB()).encryptor()

    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    
    return ciphertext , iv

def decrypt(data:str , key:bytes , mode_cbc:bool , iv:bytes | None = None)->bytes:
    if mode_cbc:
        decryptor = Cipher(algorithms.AES(key) , modes.CBC(iv)).decryptor()
    else:    
        decryptor = Cipher(algorithms.AES(key) , modes.ECB()).decryptor()
    decryptedData = decryptor.update(data) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    original_text = unpadder.update(decryptedData)+ unpadder.finalize()
    return original_text

def ans_4_5_6():
    with open('encryption\\original.txt' , "r") as file :
        plain = file.read().encode()
        key = ans_3()
        cipher , iv = encrypt(plain, key , True)

    with open('encryption\\encrypted.txt' , "wb") as file :
        file.write(cipher)
        
    with open('encryption\\iv.txt' , "wb") as file :
        file.write(iv)

    with open('encryption\\iv.txt' , "rb") as file :
        iv = file.read()

    with open('encryption\\encrypted.txt' , "rb") as file :
        cipher = file.read()

    decrypted = decrypt(cipher, key, True, iv)

    with open('encryption\\decrypted.txt', "wb") as file:
        file.write(decrypted)

    return


def des_encrypt_ecb(data: bytes, key: bytes) -> bytes:
    padder = padding.PKCS7(algorithms.TripleDES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()
    encryptor = Cipher(algorithms.TripleDES(key), modes.ECB()).encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    return ciphertext

def ans_7():
    key = b"8bytekey"  
    plaintext = b"Hello DES!"
    ciphertext = des_encrypt_ecb(plaintext, key)
    print(ciphertext)
    return

def ans_9():
    print("=== Mini AES Encryption Tool ===")

    plaintext = input("Enter text to encrypt: ").encode()
    key_input = input("Enter AES key (16/24/32 bytes). Type 'hex:' to supply hex: ")

    if key_input.startswith("hex:"):
        key = bytes.fromhex(key_input[4:])
    else:
        key = key_input.encode()

    if len(key) not in (16, 24, 32):
        print("ERROR: AES key must be 16, 24, or 32 bytes.")
        return
    mode_choice = input("Use CBC mode? (y/n): ").strip().lower()
    mode_cbc = (mode_choice == "y")
    ciphertext, iv = encrypt(plaintext, key, mode_cbc)
    filename = "encryption\\encrypted_output.bin"
    with open(filename, "wb") as f:
        if iv:
            f.write(iv + ciphertext)
        else:
            f.write(ciphertext)

    print("\n=== Encryption Complete ===")
    print(f"Ciphertext saved to: {filename}")
    if iv:
        print(f"IV (hex): {iv.hex()}")
    print(f"Ciphertext (hex): {ciphertext.hex()}")
    print("===========================")
    return


def main():
    # ans_1()
    # ans_2()
    # ans_3()
    # ans_4_5_6()
    # ans_7()
    # ans_8()
    ans_9()
    # ans_10()
    return


if __name__ == "__main__":
    main()