import time
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Key generation
start = time.time()
key = get_random_bytes(16)
end = time.time()
print("Key generation time: ", end - start)

# Encryption
start = time.time()
cipher = AES.new(key, AES.MODE_EAX)
plaintext = b'This is a test.'
ciphertext, tag = cipher.encrypt_and_digest(plaintext)
end = time.time()
print("Encryption time: ", end - start)

# Decryption
start = time.time()
cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
decryptedtext = cipher_dec.decrypt_and_verify(ciphertext, tag)
end = time.time()
print("Decryption time: ", end - start)

print("Original message: ", plaintext)
print("Encrypted message: ", ciphertext)
print("Decrypted message: ", decryptedtext)