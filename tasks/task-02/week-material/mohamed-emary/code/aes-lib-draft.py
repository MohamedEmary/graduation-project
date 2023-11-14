# Import the AES module from the pycrypto library
from Crypto.Cipher import AES


# Define a class for the AES cipher
class AESCipher:

    # Initialize the class with a key
    def __init__(self, key):
        # Generate a 256-bit hash from the key using SHA-256
        self.key = key.encode("utf-8")
        self.key = hashlib.sha256(self.key).digest()

        # Set the block size to 128 bits (16 bytes)
        self.block_size = 16

    # Define a method to pad the plain text
    def __pad(self, plain_text):
        # Calculate how many bytes are needed to make the plain text a multiple of 16
        padding = self.block_size - len(plain_text) % self.block_size

        # Append that many bytes to the plain text, each byte having the value of the padding
        return plain_text + padding * chr(padding)

    # Define a method to unpad the plain text
    def __unpad(self, plain_text):
        # Get the last byte of the plain text
        last_byte = plain_text[-1]

        # Check if the last byte is a valid padding value (between 1 and 16)
        if isinstance(last_byte, int) and last_byte > 0 and last_byte <= self.block_size:
            # Remove that many bytes from the end of the plain text
            return plain_text[:-last_byte]
        else:
            # If not, return the plain text as it is
            return plain_text

    # Define a method to encrypt the plain text
    def encrypt(self, plain_text):
        # Pad the plain text
        plain_text = self.__pad(plain_text)

        # Create an AES cipher object with the key and a random initialization vector (IV)
        cipher = AES.new(self.key, AES.MODE_CBC)

        # Encrypt the plain text with the cipher and prepend the IV to the ciphertext
        ciphertext = cipher.iv + cipher.encrypt(plain_text.encode("utf-8"))

        # Return the ciphertext as a base64 encoded string
        return base64.b64encode(ciphertext).decode("utf-8")

    # Define a method to decrypt the ciphertext
    def decrypt(self, ciphertext):
        # Decode the ciphertext from base64 encoding
        ciphertext = base64.b64decode(ciphertext)

        # Extract the IV from the first 16 bytes of the ciphertext
        iv = ciphertext[:self.block_size]

        # Create an AES cipher object with the key and the IV
        cipher = AES.new(self.key, AES.MODE_CBC, iv)

        # Decrypt the ciphertext with the cipher and unpad the plain text
        plain_text = cipher.decrypt(ciphertext[self.block_size:])
        plain_text = self.__unpad(plain_text.decode("utf-8"))

        # Return the plain text as a string
        return plain_text


# Create an instance of the AESCipher class with a secret key
aes_cipher = AESCipher("my secret key")

# Encrypt some plain text and print it
encrypted = aes_cipher.encrypt("Hello world!")
print(encrypted)

# Decrypt some ciphertext and print it
decrypted = aes_cipher.decrypt(encrypted)
print(decrypted)
