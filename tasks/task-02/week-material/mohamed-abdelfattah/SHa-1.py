
import struct
import hashlib

def sha1(message):
    # Pre-processing
    original_byte_len = len(message)
    original_bit_len = original_byte_len * 8
    message += b'\x80'
    while (len(message) * 8) % 512 != 448:
        message += b'\x00'
    message += struct.pack('>Q', original_bit_len)

def sha1(message):
  
  h0 = 0x67452301
  h1 = 0xEFCDAB89
  h2 = 0x98BADCFE
  h3 = 0x10325476
  h4 = 0xC3D2E1F0

  msg = bytearray(message)
  orig_byte_len = len(msg)
  msg.append(0x80)
  
  while (len(msg) % 64) != 56:
    msg.append(0x00)

  msg += struct.pack('>Q', orig_byte_len * 8)
  
  for chunk_offset in range(0, len(msg), 64):
    chunk = msg[chunk_offset:chunk_offset + 64]
    h0, h1, h2, h3, h4 = process_chunk(chunk, h0, h1, h2, h3, h4)

  return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)

def left_rotate(n, b):
  return ((n << b) | (n >> (32 - b))) & 0xffffffff

def process_chunk(chunk, h0, h1, h2, h3, h4):

  w = [0] * 80

  for n in range(0, 16):
    w[n] = struct.unpack('>I', chunk[n*4:n*4 + 4])[0]
  
  for n in range(16, 80):
    w[n] = left_rotate(w[n-3] ^ w[n-8] ^ w[n-14] ^ w[n-16], 1)

  a = h0
  b = h1
  c = h2
  d = h3
  e = h4

  for i in range(0, 80):

    if 0 <= i <= 19:
      f = (b & c) | ((~b) & d)
      k = 0x5A827999
    elif 20 <= i <= 39:
      f = b ^ c ^ d
      k = 0x6ED9EBA1
    elif 40 <= i <= 59:
      f = (b & c) | (b & d) | (c & d) 
      k = 0x8F1BBCDC
    elif 60 <= i <= 79:
      f = b ^ c ^ d
      k = 0xCA62C1D6

    temp = left_rotate(a, 5) + f + e + k + w[i] & 0xffffffff
    e = d
    d = c
    c = left_rotate(b, 30)
    b = a
    a = temp

  h0 = h0 + a & 0xffffffff
  h1 = h1 + b & 0xffffffff 
  h2 = h2 + c & 0xffffffff
  h3 = h3 + d & 0xffffffff
  h4 = h4 + e & 0xffffffff

  return h0, h1, h2, h3, h4


message = b'MOHAMED ABD ELFATH AHMED ABD ELFATH'
print(sha1(message))
