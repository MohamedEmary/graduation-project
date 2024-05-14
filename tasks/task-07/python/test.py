# **Import The Useable Libraries:**
from decimal import Decimal
import numpy as np
import string
import random
from time import time


# **Define The Global Variables**
text = None
textSize = 5
# textSize = 5000


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


class BiNew(object):
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
            chunk = self.text[beg:]
            normalized_values.append(
                self.get_normalized_value(self.encode_and_get_int_values(chunk)))
        return normalized_values

    def get_interger_values(self, normalized_values):
        interger_values = []
        for normalized_value in normalized_values:
            interger_values.append(
                self.get_inverse_normalized_value(normalized_value))
        return interger_values

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
            result = Decimal(result) * (Decimal(target) -
                                        Decimal(self.x[i])) + Decimal(self.coefs[i])
        return result - normalized_value

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

    def encryption(self):
        cipher_text = []
        self.newton_forward_coefficients()
        normalized_values = self.get_normalized_values()
        for normalized_value in normalized_values:
            cipher_text.append(self.find_roots_secant(
                self.x[0], self.x[-1], normalized_value))  # Secant
        return cipher_text

    def decryption(self, cipher_text):
        text = []
        for root in cipher_text:
            norm = self.evaluate_interpolated_value(root)
            inverse = self.get_inverse_normalized_value(norm)
            text.append(self.decode_and_get_string(Decimal(round(inverse))))
        return "".join(text)


[text, xpoints, ypoints] = [
    'kaVELmZdFztIZKgNwVtmIlERBwnlNLQBxpRcezrbbwladouabfuawvfiyawvjLpghbwJg',
    [17, 17.5, 18.0, 18.5, 19.0, 19.5],
    [45, 45.5, 46.0, -46.5, -47.0, -47.5]
]

obj = BiNew(text, xpoints, ypoints)
ciper_text = obj.encryption()
decrypted_text = obj.decryption(ciper_text)
print(decrypted_text)
