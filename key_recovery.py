from base64 import b64encode, b64decode
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from base64 import b64decode
import glob
import os

# decrypt AES_CBC Key
with open("key.bin", "rb") as f:
    private_key = RSA.import_key(
        open("ransomprvkey.pem").read())
    cipher_rsa = PKCS1_OAEP.new(private_key)
    decrypted_key = cipher_rsa.decrypt(f.read())
    with open("key.txt", "w") as f1:
        li = b64encode(decrypted_key).decode('utf-8')
        f1.write(li)


data = open('key.txt', 'r').read()
decrypted_aes_key = b64decode(data)

print("Key successfully recovered")
