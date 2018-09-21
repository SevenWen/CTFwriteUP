import binascii


hexstr = list('00000000')
# binstr = binascii.unhexlify(hexstr)
# a=b'\x00\x00\x00\x00'
a=0
hexnum='0123456789abcdef'
hexlist=list(hexnum)

while a<= int("0xffffffff",0):
	# b=b'\x01'
	hbytes=(a).to_bytes(8, byteorder='big')
	print(hbytes)
	a=a+1
	# binstr = binascii.unhexlify(hexstr)
	# print(binstr)
	pass

# for i in range(8):
# 	for j in hexlist:
# 		hexstr[i]=j
# 		print(hexstr)