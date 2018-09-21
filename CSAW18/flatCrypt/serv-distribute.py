import zlib
import os

from Crypto.Cipher import AES
from Crypto.Util import Counter

ENCRYPT_KEY = bytes.fromhex('0000000000000000000000000000000000000000000000000000000000000000')
# Determine this key.
# Character set: lowercase letters and underscore
PROBLEM_KEY = 'not_the_flag'

def encrypt(data, ctr):
    compressed=zlib.compress(data)
    print("compressed:",compressed)
    crypto=AES.new(ENCRYPT_KEY, AES.MODE_CTR, counter=ctr)
    cipher=crypto.encrypt(compressed)
    return crypto.decrypt(cipher)

while True:
    f = input("Encrypting service\n")

    if len(f) < 20:
        continue
    aa=os.urandom(8)
    enc = encrypt(bytes((PROBLEM_KEY + f).encode('utf-8')), Counter.new(64, prefix=aa))

    print("%s%s" %(enc, chr(len(enc))))