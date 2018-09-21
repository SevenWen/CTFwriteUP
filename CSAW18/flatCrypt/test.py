import zlib
import os

from Crypto.Cipher import AES
from Crypto.Util import Counter

ENCRYPT_KEY = bytes.fromhex('0000000000000000000000000000000000000000000000000000000000000000')
# Determine this key.
# Character set: lowercase letters and underscore
PROBLEM_KEY = 'not_the_flag'

i=0

def decrypt(data, ctr):
    return AES.new(ENCRYPT_KEY, AES.MODE_CTR, counter=ctr).decrypt(data)

while i<= int("0xffffffff",0):
    aa= (i).to_bytes(8, byteorder='big')
    print(aa)
    # aa=b'\xaeM\xee\xc4\x96a\x80\xc7'
    ctr=Counter.new(64, prefix=aa)
    crypto=AES.new(ENCRYPT_KEY, AES.MODE_CTR, counter=ctr)
    cipher=b'_|\x8d\xe3b\xfe\x9esL\t*(s\xc3g\x84\xf9\x9a\x0bZ\xdc$\x1d\xeb`>g\xa2R\x87\x19\xe6\x86\xd8z\xf2\x18\xd2'
    dec = decrypt(cipher, Counter.new(64, prefix=aa))

    try:
        print(zlib.decompress(dec))
        break
    except:
        pass

    i=i+1