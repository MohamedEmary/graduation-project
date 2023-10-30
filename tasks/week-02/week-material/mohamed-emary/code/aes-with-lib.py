'''
Each programming language offers its own implementation of the AES
algorithm. While implementing AES from scratch is a possibility,
it is highly recommended to use known libraries instead if you are
not a cybersecurity expert: the slightest error in your code would
result in data leaks!
'''


from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


def encrypt(plaintext, key):
    # Generate a random initialization vector (IV)
    iv = get_random_bytes(16)

    # Create an AES cipher object with the provided key and AES.MODE_CBC mode
    # In CBC Each block is XORed with the previous ciphertext block before
    # encryption.
    cipher = AES.new(key, AES.MODE_CBC, iv)  # ECB CTR

    # Pad the plaintext to be a multiple of 16 bytes (AES block size)
    padded_plaintext = pad(plaintext.encode(), 16)

    # Encrypt the padded plaintext
    ciphertext = cipher.encrypt(padded_plaintext)

    # Return the IV and ciphertext as a tuple
    return iv + ciphertext


def decrypt(ciphertext, key):
    # Extract the IV from the ciphertext
    iv = ciphertext[:16]

    # Create an AES cipher object with the provided key, AES.MODE_CBC mode, and the extracted IV
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt the ciphertext
    decrypted_data = cipher.decrypt(ciphertext[16:])

    # Unpad the decrypted data
    plaintext = unpad(decrypted_data, 16)

    # Decode the plaintext and return it as a string
    return plaintext.decode()


# Example usage:
key = get_random_bytes(16)  # Generate a random 128-bit key
plaintext = "Hello, AES!"  # The text to be encrypted

# Encrypt the plaintext
ciphertext = encrypt(plaintext, key)
print("Encrypted:", ciphertext)

# Decrypt the ciphertext
decrypted_text = decrypt(ciphertext, key)
print("Decrypted:", decrypted_text)
