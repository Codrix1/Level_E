import rsa

with open("encryption\\public.pem","rb") as file:
    public_key = rsa.PublicKey.load_pkcs1(file.read())
with open("encryption\\private.pem","rb") as file:
    private_key = rsa.PrivateKey.load_pkcs1(file.read())


def ans_1():
    public_key  , private_key = rsa.newkeys(1024)
    with open("encryption\\public.pem","wb") as file:
        file.write(public_key.save_pkcs1("PEM"))
    with open("encryption\\private.pem","wb") as file:
        file.write(private_key.save_pkcs1("PEM"))

    return

def ans_2():
    msg = "this is a short message that i will encrypt with the keys"
    encrypted = rsa.encrypt(msg.encode() , public_key )
    print("this is the encrypted message: "+str(encrypted) +"\n")

    decrypted = rsa.decrypt(encrypted , private_key)
    print("this is the decrypted message: "+str(decrypted))
    return 

def ans_3_4():
    msg = "this is a short message that i will sign with the keys"
    signiture = rsa.sign(msg.encode(),private_key,"MD5")
    print(signiture)
    print(rsa.verify(msg.encode() , signiture , public_key))
    return

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256

def ans_6():
    key = RSA.generate(2048)
    public_key = key.publickey()
    cipher = PKCS1_OAEP.new(public_key, hashAlgo=SHA256)
    ciphertext = cipher.encrypt(b"hello world")

    dec_cipher = PKCS1_OAEP.new(key, hashAlgo=SHA256)
    plaintext = dec_cipher.decrypt(ciphertext)

    print(plaintext)

def main():
    # ans_1()
    # ans_2()
    # ans_3_4()
    # ans_4()
    # ans_5()
    ans_6()    
    # ans_7()
    # ans_8()
    # ans_9()
    # ans_10()
    return


if __name__ == "__main__":
    main()