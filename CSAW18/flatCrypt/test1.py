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
    # aa=b'\xaeM\xee\xc4\x96a\x80\xc7'
    ctr=Counter.new(64, prefix=aa)
    crypto=AES.new(ENCRYPT_KEY, AES.MODE_CTR, counter=ctr)
    cipher=b'\xd4b\xa1/\xd9,\xe1\xef\nD\xbbv\x14\xf9\xf6\x83d\xe6\xdeg\x19\xc2\xd3\xa2\xfb\xcb\xbf\xc9\x85\x8e\x96\xc7V\t'
    dec = decrypt(cipher, Counter.new(64, prefix=aa))

    try:
        print(zlib.decompress(dec))
        break
    except:
        pass

    i=i+1