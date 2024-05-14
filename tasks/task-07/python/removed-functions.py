import numpy as np
from decimal import Decimal


def decode_and_get_strings(self, int_values):
    strings = []
    for int_value in int_values:
        int_value = np.ceil(int_value)
        byte_representation = int_value.to_bytes(
            (int_value.bit_length() + 7) // 8, byteorder='big')
        text = byte_representation.decode('utf-8')
        strings.append(text)
    return "".join(strings)


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


def get_interger_values(self, normalized_values):
    interger_values = []
    for normalized_value in normalized_values:
        interger_values.append(
            self.get_inverse_normalized_value(normalized_value))
    return interger_values


def string_to_integer(s):
    # Encode the string into bytes using UTF-8
    encoded_bytes = s.encode('utf-8')
    # Convert bytes to integer
    integer_value = int.from_bytes(encoded_bytes, byteorder='big')
    return integer_value
