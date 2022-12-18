from base64 import b64encode, b64decode
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from base64 import b64decode
import glob
import os

iv = b'0123456789abcdef'

data = open('key.txt', 'r').read()
decrypted_aes_key = b64decode(data)

os.chdir(r'../Assignment1')
myNewFile = glob.glob('*')

for files in myNewFile:
    if files.endswith('.enc'):
        pre, ext = os.path.splitext(files)
        newFile = pre + ".txt"
        with open(files) as f:
            with open(newFile, "w") as f1:
                for line in f:
                    try:
                        cipherText = b64decode(line)
                        cipher = AES.new(decrypted_aes_key, AES.MODE_CBC, iv)
                        plainText = unpad(cipher.decrypt(cipherText), AES.block_size)
                        decodedLine = plainText.decode('utf-8')
                        f1.write(decodedLine)
                    except ValueError as KeyError:
                        print("Incorrect decryption")

os.chdir(r'../Assignment1')
myFiles = glob.glob('*.enc')

for files in myFiles:
    os.remove(files)

print("File successfully recovered")

