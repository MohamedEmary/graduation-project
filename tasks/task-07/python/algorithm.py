import scienceplots
from decimal import Decimal, getcontext
import warnings
import numpy as np
import pandas as pd
import string
import random
from time import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import base64
from Crypto.Util.Padding import unpad
import matplotlib.pyplot as plt
# %matplotlib inline


warnings.filterwarnings("ignore")
pd.set_option("display.max_rows", 50)
pd.set_option("display.max_columns", 500)
plt.rcParams.update({'font.size': 12})
plt.style.use(['science', 'no-latex'])
plt.rcParams['font.family'] = 'Times New Roman'


# **Define The Global Variables**
text = None
textSize = 5000


degrees = list(range(2, 7, 1))
polynomials = []
encryptionTime = []
decryptionTime = []
totalTime = []


# **Define The Global Functions:**
def get_random_8chars(chars_length, n_sambles):
    random_chars = []
    for i in range(0, n_sambles, 1):
        letters = string.ascii_letters
        random_chars.append("".join(random.choice(letters)
                            for _ in range(chars_length)))
    return "".join(random_chars)


class IBGA(object):
    def __init__(self, text, x, y):
        if type(text) != str or len(x) != len(y):
            raise ValueError("Invalid Parameters")
        self.text = text
        self.len_text = len(text)
        self.x = [Decimal(i) for i in x]
        self.y = [Decimal(i) for i in y]
        self.coefs = None
        self.maximium_8utf_chars = Decimal(597351581456640298090110)
        self.minimum_8utf_chars = Decimal(151708338147718170943520)
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
        chunks = self.len_text // 10
        beg, end = 0, 0
        if chunks:
            end = 10
            for i in range(0, chunks, 1):
                chunk = self.text[beg: end]
                normalized_values.append(
                    self.get_normalized_value(self.encode_and_get_int_values(chunk)))
                beg = end
                end = beg + 10
        if (self.len_text / 10) % 1 != 0:
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

    def bisection_method(self, a, b, normalized_value, tol=Decimal(10 ** -38)):
        if self.evaluate_interpolated_value(a, normalized_value) * self.evaluate_interpolated_value(b, normalized_value) > 0:
            raise ValueError(
                "The function values at the endpoints must have different signs.")
        for i in range(40):
            midpoint = (a + b) / Decimal(2)
            if self.evaluate_interpolated_value(midpoint, normalized_value) == Decimal(0):
                return midpoint
            elif self.evaluate_interpolated_value(midpoint, normalized_value) * self.evaluate_interpolated_value(a, normalized_value) < 0:
                b = midpoint
            else:
                a = midpoint
        return midpoint

    def find_roots_secant(self, x0, x1, normalized_value, tol=Decimal(10 ** -17), max_iter=16):
        x_prev = Decimal(x0)
        x_curr = Decimal(x1)
        for i in range(max_iter):
            fx_prev = self.evaluate_interpolated_value(
                x_prev, normalized_value)
            fx_curr = self.evaluate_interpolated_value(
                x_curr, normalized_value)
            if fx_curr - fx_prev == 0:
                raise ValueError(
                    "Secant method cannot converge. Division by zero.")
            x_next = x_curr - fx_curr * (x_curr - x_prev) / (fx_curr - fx_prev)
            x_prev = x_curr
            x_curr = x_next
            if abs(fx_curr) < tol:
                return x_curr
        return x_curr

    def find_roots_false_position(self, a, b, normalized_value, tol=Decimal(10 ** -17), max_iter=21):
        if self.evaluate_interpolated_value(a, normalized_value) * self.evaluate_interpolated_value(b, normalized_value) > 0:
            raise ValueError(
                "The function values at the endpoints must have different signs.")
        for i in range(max_iter):
            fa = self.evaluate_interpolated_value(a, normalized_value)
            fb = self.evaluate_interpolated_value(b, normalized_value)
            if fa == Decimal(0):
                return a
            if fb == Decimal(0):
                return b
            x_next = (a * fb - b * fa) / (fb - fa)
            fx_next = self.evaluate_interpolated_value(
                x_next, normalized_value)
            if abs(fx_next) < tol:
                return x_next
            if fx_next * fa < 0:
                b = x_next
            else:
                a = x_next
        return (a + b) / Decimal(2)

    def encryption(self):
        cipher_text = []
        self.newton_forward_coefficients()
        normalized_values = self.get_normalized_values()
        for normalized_value in normalized_values:
            cipher_text.append(self.find_roots_secant(
                self.x[0], self.x[-1], normalized_value))  # Secant
        return cipher_text

    def dencryption(self, cipher_text):
        text = []
        for root in cipher_text:
            norm = self.evaluate_interpolated_value(root)
            inverse = self.get_inverse_normalized_value(norm)
            text.append(self.decode_and_get_string(Decimal(round(inverse))))
        return "".join(text)


# Generate Random Polynomial:
polynomials = []
for i in range(0, len(degrees), 1):
    xpoints = []
    ypoints = []
    x = random.randint(1, 50)
    y = random.randint(1, 50)
    xpoints.append(x)
    ypoints.append(y)
    for j in range(0, degrees[i], 1):
        x += 0.5
        y += 0.5
        xpoints.append(x)
        ypoints.append(y)
    midY = int(len(ypoints) / 2)
    ypoints[midY:] = [-1 * k for k in ypoints[midY:]]
    polynomials.append((xpoints, ypoints))


for i in range(0, len(polynomials), 1):
    print("====================================")
    print(f"X Points: {polynomials[i][0]}")
    print(f"Y Points: {polynomials[i][1]}")
    print("====================================")


# Encryption Analysis:
text = get_random_8chars(10, textSize)


for i in range(0, len(polynomials), 1):
    xpoints = polynomials[i][0]
    ypoints = polynomials[i][1]
    obj = IBGA(text, xpoints, ypoints)

    ibga_en_beg = time()
    ciper_text = obj.encryption()
    ibga_en_end = time()
    en_time = ibga_en_end - ibga_en_beg
    encryptionTime.append(en_time)

    ibga_den_beg = time()
    text_dencryption = obj.dencryption(ciper_text)
    ibga_den_end = time()
    den_time = ibga_den_end - ibga_den_beg
    decryptionTime.append(den_time)

    totalTime.append(en_time + den_time)
    print(text_dencryption == text)
