# # Import The Useable Libraries:
import os
from aes import encrypt, decrypt
from decimal import Decimal
import warnings
import numpy as np
import pandas as pd
import string
import random
from time import time
import matplotlib.pyplot as plt
# %matplotlib inline

# # **Define The Global Notebook Settings:**

warnings.filterwarnings("ignore")
pd.set_option("display.max_rows", 50)
pd.set_option("display.max_columns", 500)
plt.rcParams.update({'font.size': 14})
plt.style.use(['science', 'no-latex'])
plt.rcParams['font.family'] = 'Times New Roman'

# # **Define The Global Variables:**


def get_random_8chars(chars_length, n_sambles):
    random_chars = []
    for i in range(0, n_sambles, 1):
        letters = string.ascii_letters
        random_chars.append("".join(random.choice(letters)
                            for _ in range(chars_length)))
    return "".join(random_chars)


polynomials = [
    ([2, 2.5, 3], [2, -2, -3]),
    ([3, 3.5, 4, 4.5], [3, 3.7, -4, -4.5]),
    ([4, 4.5, 5, 5.5, 6], [-4, 4, 5, -5.5, -6]),
    ([5, 5.5, 6, 6.5, 7, 7.5], [5, 5.3, 6, -6.5, -7, -7.5]),
    ([6, 6.5, 7, 7.5, 8, 8.5, 9], [6, 6.7, 7, 7.5, -8, -8.5, -9]),
]

Degrees = []
for poly in polynomials:
    Degrees.append(len(poly[0]) - 1)

block_size = 10

min_block = ' '*block_size
max_block = '~'*block_size

min_rep = int.from_bytes(
    min_block.encode('utf-8'), byteorder='big')
max_rep = int.from_bytes(
    max_block.encode('utf-8'), byteorder='big')

print(min_rep, max_rep)

text_samples = []

text_sizes = [50, 75, 100, 125, 150,
              175, 200, 225, 250, 275, 300]

# text_sizes = [5000, 7500, 10000, 12500, 15000,
#               17500, 20000, 22500, 25000, 27500, 30000]

for size in text_sizes:
    text_samples.append(get_random_8chars(block_size, size))

secant_different_sizes_enc = []
secant_different_sizes_dec = []
secant_different_sizes_total = []

secant_different_deg_enc = []
secant_different_deg_dec = []
secant_different_deg_total = []

# ================

aes_different_sizes_enc = []
aes_different_sizes_dec = []
aes_different_sizes_total = []


aes_different_keys_enc = []
aes_different_keys_dec = []
aes_different_keys_total = []

# # **Define The Global Classes:**


class ibga(object):
    def __init__(self, text, x, y):
        if type(text) != str or len(x) != len(y):
            raise ValueError("Invalid parameters passed")
        self.text = text
        self.len_text = len(text)
        self.x = [Decimal(i) for i in x]
        self.y = [Decimal(i) for i in y]
        self.coefs = None
        self.maximium_8utf_chars = Decimal(max_rep)
        self.minimum_8utf_chars = Decimal(min_rep)
        self.len_x = len(x)

    def set_text(self, text):
        if type(text) != str:
            raise ValueError("Invalid text type passed")
        self.text = text

    def set_x_y(self, x, y):
        if len(x) != len(y):
            raise ValueError("Invalid x, y points size passed")
        self.x = [Decimal(i) for i in x]
        self.y = [Decimal(i) for i in y]
        self.len_x = len(x)
        self.coefs = None

    def encode_and_get_int_values(self, chunk):
        byte_representation = chunk.encode('utf-8')
        integer_representation = int.from_bytes(
            byte_representation, byteorder='big')
        return integer_representation

    def get_normalized_value(self, integer_value):
        decimal_value = Decimal(integer_value)
        normalized_value = (decimal_value - self.minimum_8utf_chars) / \
            (self.maximium_8utf_chars - self.minimum_8utf_chars)
        return normalized_value

    def get_inverse_normalized_value(self, normalized_value):
        integer_value = (normalized_value *
                         (self.maximium_8utf_chars - self.minimum_8utf_chars)) + self.minimum_8utf_chars
        return integer_value

    def get_normalized_values(self):
        normalized_values = []
        chunks = self.len_text // block_size
        beg, end = 0, 0
        if chunks:
            end = block_size
            for i in range(0, chunks, 1):
                chunk = self.text[beg: end]
                normalized_values.append(
                    self.get_normalized_value(self.encode_and_get_int_values(chunk)))
                beg = end
                end = beg + block_size
        if (self.len_text / block_size) % 1 != 0:
            chunk = self.text[end:]
            normalized_values.append(
                self.get_normalized_value(self.encode_and_get_int_values(chunk)))
        return normalized_values

    def get_interger_values(self, normalized_values):
        interger_values = []
        for normalized_value in normalized_values:
            interger_values.append(
                self.get_inverse_normalized_value(normalized_value))
        return interger_values

    def decode_and_get_strings(self, int_values):
        strings = []
        for int_value in int_values:
            int_value = np.ceil(int_value)
            byte_representation = int_value.to_bytes(
                (int_value.bit_length() + 7) // 8, byteorder='big')
            text = byte_representation.decode('utf-8')
            strings.append(text)
        return "".join(strings)

    def decode_and_get_string(self, int_value):
        int_value = np.ceil(int_value)
        byte_representation = int_value.to_bytes(
            (int_value.bit_length() + 7) // 8, byteorder='big')
        return (byte_representation.decode('utf-8'))

    def newton_forward_coefficients(self):
        n = len(self.x)
        coefficients = np.zeros(n, dtype=Decimal)
        for i in range(n):
            coefficients[i] = Decimal(self.y[i])
        for j in range(1, n):
            for i in range(n - 1, j - 1, -1):
                coefficients[i] = (coefficients[i] - coefficients[i - 1]) / \
                    (self.x[i] - self.x[i - j])
        self.coefs = coefficients

    def evaluate_interpolated_value(self, target, normalized_value=Decimal(0)):
        n = self.len_x
        result = Decimal(self.coefs[-1])
        for i in range(n - 2, -1, -1):
            result = Decimal(result) * \
                (Decimal(target) - Decimal(self.x[i])) + Decimal(self.coefs[i])
        return result - normalized_value

    def evaluate_derivative(self, x, normalized_value):
        n = len(self.coefs) - 1
        result = Decimal(n) * (self.coefs[-1] - normalized_value)
        for i in range(n - 1, 0, -1):
            result = result * \
                (Decimal(x) - Decimal(self.x[i])) + Decimal(i) * self.coefs[i]
        return result

    def secant(self, x0, x1, normalized_value, tol=Decimal(10 ** -17)):
        x_prev = Decimal(x0)
        x_curr = Decimal(x1)

        while abs(x_curr - x_prev) > tol:
            fx_prev = self.evaluate_interpolated_value(
                x_prev, normalized_value)
            fx_curr = self.evaluate_interpolated_value(
                x_curr, normalized_value)

            if fx_curr - fx_prev == 0:
                raise ValueError(
                    "Secant method cannot converge. Division by zero.")

            x_next = x_curr - fx_curr * (x_curr - x_prev) / (fx_curr - fx_prev)
            x_prev, x_curr = x_curr, x_next

        return x_curr

    def encryption(self, root_finding_algorithm='secant'):
        cipher_text = []
        self.newton_forward_coefficients()
        normalized_values = self.get_normalized_values()
        algorithms = {
            'secant': self.secant,
        }
        if root_finding_algorithm not in algorithms:
            raise ValueError(
                f"Invalid algorithm_name. Expected one of: {', '.join(algorithms.keys())}")

        selected_algorithm = algorithms[root_finding_algorithm]

        for normalized_value in normalized_values:
            cipher_text.append(selected_algorithm(
                self.x[0], self.x[-1], normalized_value))

        return cipher_text

    def decryption(self, cipher_text):
        text = []
        for root in cipher_text:
            norm = self.evaluate_interpolated_value(root)
            inverse = self.get_inverse_normalized_value(norm)
            text.append(self.decode_and_get_string(Decimal(round(inverse))))
        return "".join(text)

# # Get The Encryption & Decrytion & Total Times For Bisection , Secant Hyprid With Differrent Polynomials Degree 2 : 6
#
# > **Hint**:
# > 1)  According To The Useable Root Finding Algorithm Uncomment Its Callable Function Inside The Encryption Function.
# > 2) Root Finding Algorithms Analysis Woerking With Block Size 4bytes For (Bisection , False Position).

# ### Get Encryption , Decryption , Total Times When Using Secant:


poly = polynomials[3]
for text in text_samples:
    obj = ibga(text, poly[0], poly[1])
    ibga_en_beg = time()
    ciper_text = obj.encryption('secant')
    ibga_en_end = time()
    enc_time = ibga_en_end - ibga_en_beg
    secant_different_sizes_enc.append(enc_time)

    ibga_dec_beg = time()
    text_decryption = obj.decryption(ciper_text)
    ibga_dec_end = time()
    dec_time = ibga_dec_end - ibga_dec_beg
    secant_different_sizes_dec.append(dec_time)

    secant_different_sizes_total.append(enc_time + dec_time)
    print(text_decryption == text)

print('='*10)

text = text_samples[-1]
for poly in polynomials:
    obj = ibga(text, poly[0], poly[1])
    ibga_en_beg = time()
    ciper_text = obj.encryption('secant')
    ibga_en_end = time()
    en_time = ibga_en_end - ibga_en_beg
    secant_different_deg_enc.append(en_time)

    ibga_dec_beg = time()
    text_decryption = obj.decryption(ciper_text)
    ibga_dec_end = time()
    dec_time = ibga_dec_end - ibga_dec_beg
    secant_different_deg_dec.append(dec_time)

    secant_different_deg_total.append(en_time + dec_time)
    print(text_decryption == text)

# ### Using AES:

key = 'aMkjcMd#%)45'

keys = []
for i in range(len(polynomials)):
    keys.append(key*(i+1))

key = keys[1].encode('utf-8')
for text in text_samples:
    aes_enc_beg = time()
    ciphertext = encrypt(key, text.encode('utf-8'))
    aes_enc_end = time()

    enc_time = aes_enc_end - aes_enc_beg
    aes_different_sizes_enc.append(enc_time)

    aes_dec_beg = time()
    decrypted_text = decrypt(key, ciphertext)
    aes_dec_end = time()

    dec_time = aes_dec_end - aes_dec_beg
    aes_different_sizes_dec.append(dec_time)
    aes_different_sizes_total.append(enc_time + dec_time)

    print(decrypted_text.decode('utf-8') == text)


print('='*10)

text = text_samples[-1]
for key in keys:
    key = key.encode('utf-8')
    aes_enc_beg = time()
    ciphertext = encrypt(key, text.encode('utf-8'))
    aes_enc_end = time()

    enc_time = aes_enc_end - aes_enc_beg
    aes_different_keys_enc.append(enc_time)

    aes_dec_beg = time()
    decrypted_text = decrypt(key, ciphertext)
    aes_dec_end = time()

    dec_time = aes_dec_end - aes_dec_beg
    aes_different_keys_dec.append(dec_time)
    aes_different_keys_total.append(enc_time + dec_time)

    print(decrypted_text.decode('utf-8') == text)

# ---

# Polynomial Deg & Text Array Size
print(polynomials)
polynomials_degrees = []
for poly in polynomials:
    polynomials_degrees.append(len(poly[0]) - 1)

print(polynomials_degrees)
print(text_sizes)

# Time Results
print(secant_different_sizes_enc)
print(secant_different_sizes_dec)
print(secant_different_sizes_total)
print(secant_different_deg_enc)
print(secant_different_deg_dec)
print(secant_different_deg_total)

print('='*10)

print(aes_different_sizes_enc)
print(aes_different_sizes_dec)
print(aes_different_sizes_total)
print(aes_different_keys_enc)
print(aes_different_keys_dec)
print(aes_different_keys_total)


# Flatten the list of degrees and keys
degrees = [len(poly[0]) - 1 for poly in polynomials]
key_sizes = [len(key) for key in keys]


# Save the results to a CSV file
# Combine all results into a DataFrame
results = {
    'text_sizes': text_sizes,
    'secant_different_sizes_enc': secant_different_sizes_enc,
    'secant_different_sizes_dec': secant_different_sizes_dec,
    'secant_different_sizes_total': secant_different_sizes_total,
    'secant_different_deg_enc': secant_different_deg_enc,
    'secant_different_deg_dec': secant_different_deg_dec,
    'secant_different_deg_total': secant_different_deg_total,
    'aes_different_sizes_enc': aes_different_sizes_enc,
    'aes_different_sizes_dec': aes_different_sizes_dec,
    'aes_different_sizes_total': aes_different_sizes_total,
    'aes_different_keys_enc': aes_different_keys_enc,
    'aes_different_keys_dec': aes_different_keys_dec,
    'aes_different_keys_total': aes_different_keys_total,
    'degrees': degrees,
    'key_sizes': key_sizes,
    'polynomials_degrees': polynomials_degrees,
}

df = pd.DataFrame({k: pd.Series(v) for k, v in results.items()})
script_dir = os.path.dirname(__file__)
df.to_csv(os.path.join(script_dir, 'plots/results.csv'), index=False)
