import struct
import socket
import sys
import collections
 
HOST = 'crypto.chal.csaw.io'
PORT = 8040
 
def try_val(val):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.connect((HOST, PORT))
  nonce = sock.recv(8)
  sock.send(struct.pack('I', len(val)))
  sock.send(val)
  data = sock.recv(4)
  recv_len = struct.unpack('I', data)[0]
  data = sock.recv(recv_len)
  return (nonce, data)
 
 
def get_candidate_len(can):
  nonce, data = try_val(can)
  return len(data)
 
def try_layer(prefix):
  if len(prefix) == 20:
    print "Found candidate %s!" % prefix
    return
 
  candidates = 'abcdefghijklmnopqrstuvwxyz_'
  print "Trying %s" % prefix
  sys.stdout.flush()
  samples = {}
  for c in candidates:
    val = prefix + c
    samples[val] = get_candidate_len(val*2 if len(val)>9 else val*5)
  m = mode(samples.values())
  for k in samples:
    if samples[k] == m:
      continue
    try_layer(k)
 
def mode(l):
  c = collections.Counter(l)
  return c.most_common(1)[0][0]
 
try_layer('')