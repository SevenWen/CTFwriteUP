from pwn import *
import string

candidates = string.ascii_lowercase + "_"

#flag='_a_logo_a_logoave_a_logoo' #pppgopooave_a_logoo
flag="rime_doesnt_have_a_logo"

dic={}

for char in candidates:
	conn = remote('crypto.chal.csaw.io', 8043)
	print(conn.recv())
	conn.sendline((char+flag)*3)
	out=conn.recvline()
	l=out[-2]
	dic[char]=l
	print(l,char)
	# if l<34:
	# 	print(char)
	# 	flag=flag+char
	# 	break
	conn.close()


print(dic)