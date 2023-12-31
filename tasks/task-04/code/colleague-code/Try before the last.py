# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 14:36:38 2023

@author: ebrahim elsayed
"""

import numpy as np
from scipy.interpolate import lagrange
import random


def root_finding_initial_values(f, degree, method):
    # Create a poly1d object from the polynomial coefficients
    poly = np.poly1d(f)

    coefficients = poly.coeffs  # Get the coefficients of the polynomial

    constant = coefficients[-1]  # Constant term of the polynomial

    print(constant)
    # Rest of the function remains the same
    nth_root = 0

    if 1 <= degree <= 10:
        nth_root = degree // 2
    elif 10 <= degree <= 15:
        nth_root = degree // 3
    else:
        nth_root = degree

    if nth_root == 0:
        nth_root = 1

    constant_nth_root = abs(constant) ** (1 / nth_root)

    # if constant < 0:
    # constant_nth_root = -constant_nth_root

    if method == 'bisection':
        initial_one_bi = -round(constant_nth_root)
        initial_two_bi = round(constant_nth_root)
        return initial_one_bi, initial_two_bi
    else:
        raise ValueError("Invalid method input")


def bisection(f, a, b, eps):
    n = 0
    while True:
        n += 1
        x_val = (a + b) / 2
        fx_val = f(x_val)
        fa_val = f(a)

        if abs(fx_val) <= eps:
            return x_val, fx_val, n, a, b
        elif fa_val * fx_val < 0:
            b = x_val
        else:
            a = x_val


# Generate random coefficients for the polynomial
# Randomly select an odd degree between 1 and 13
degree = random.choice(range(1, 14, 2))
# coefficients = np.random.randint(-10, 10, size=degree+1)

# Store the coefficients in a variable
# generated_coefficients = coefficients

# Generate a random plaintext
plain_text = "Hello, World! This is a sample plaintext."

# Encode the plaintext using UTF-8 encoding
plain_bytes = plain_text.encode('utf-8')

# Convert the bytes to a list of integers representing the individual byte values
# digits = [int(b) for b in plain_bytes]
digits = list(plain_bytes)

# Split the digits into blocks of 80 bits
# block_size = 80
# blocks = [digits[i:i+block_size] for i in range(0, len(digits), block_size)]

# Example usage:
print("Plaintext:", plain_text)
# print("Plaintext blocks:", blocks)

# Randomly select an odd degree between 1 and 13
degree = random.choice(range(1, 14, 2))
# degree = 5

# Use the generated coefficients in the lagrange function
# Step 2: Generate randomised polynomial through Lagrange Interpolation
x = list(range(1, degree + 2))  # x values for interpolation
y = digits[:degree+1]  # y values for interpolation
poly = lagrange(x, y)

# Print the polynomial
print("Generated Polynomial:")
print(np.poly1d(poly))

# Step 3: Generate scrambled polynomial
f = poly - digits  # Subtract x to obtain f(x) = poly - x
print(f"F = {f}")
poly_coefficients = f.coefficients  # Get the coefficients of f(x)

# You can also use the generated coefficients directly in other parts of the code
# poly_coefficients = generated_coefficients
# ... (continue using poly_coefficients as needed)

# Differentiate f(x) , The derivative of a polynomial represents the rate of change of the polynomial with respect to x. The resulting df represents the derivative of f(x).
df = np.polyder(f)
# Evaluate f(0) and take absolute value , Taking the absolute value ensures that the constant value is positive
constant = abs(f(0))

# Step 4: Guess initial values using root_finding_initial_values function
method = 'bisection'
initial_values = root_finding_initial_values(f, degree, method)

# Step 5: Apply the bisection method
error = 1e-6
root, fx, n, a, b = bisection(f, initial_values[0], initial_values[1], error)


# print("Polynomial coefficients:", poly_coefficients)
print("Plain Text:", plain_text)
print("Degree of the polynomial:", degree)
print("Root value:", root)
print("Function value at root:", fx)
print("Number of iterations:", n)
print("Updated interval [a, b]:", [a, b])
