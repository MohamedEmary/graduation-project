class ECC:
    def __init__(self, a, b, p, base_point):
        self.a = a
        self.b = b
        self.p = p
        self.base_point = base_point

    def point_addition(self, P, Q):
        if P is None:
            return Q
        if Q is None:
            return P
        x_p, y_p = P
        x_q, y_q = Q

        if P != Q:
            slope = ((y_q - y_p) * pow(x_q - x_p, -1, self.p)) % self.p
        else:
            slope = ((3 * x_p ** 2 + self.a) * pow(2 * y_p, -1, self.p)) % self.p

        x_r = (slope ** 2 - x_p - x_q) % self.p
        y_r = (slope * (x_p - x_r) - y_p) % self.p

        return x_r, y_r

    def scalar_multiply(self, k, P):
        R = None
        for bit in bin(k)[2:]:
            R = self.point_addition(R, R)
            if bit == '1':
                R = self.point_addition(R, P)
        return R

    def generate_key_pair(self):
        private_key = int.from_bytes(os.urandom(32), byteorder='big') % (self.p - 1) + 1
        public_key = self.scalar_multiply(private_key, self.base_point)
        return private_key, public_key
import os

# Define the parameters of the elliptic curve
a = 2
b = 2
p = 17
base_point = (5, 1)

# Create an ECC object with the specified parameters
ecc = ECC(a, b, p, base_point)

# Alice generates her key pair
alice_private_key, alice_public_key = ecc.generate_key_pair()

# Bob generates his key pair
bob_private_key, bob_public_key = ecc.generate_key_pair()

# Key exchange: Alice computes shared secret
shared_secret_alice = ecc.scalar_multiply(alice_private_key, bob_public_key)

# Key exchange: Bob computes shared secret
shared_secret_bob = ecc.scalar_multiply(bob_private_key, alice_public_key)

# Encrypt and decrypt a message using the shared secret (for demonstration purposes, we use XOR as a simple encryption method)
message = "Hello, ECCCCCCCCCCCCCCCCCC!"

# Encryption
encrypted_message = ''.join(chr(ord(char) ^ shared_secret_alice[0]) for char in message)

# Decryption
decrypted_message = ''.join(chr(ord(char) ^ shared_secret_bob[0]) for char in encrypted_message)

print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
