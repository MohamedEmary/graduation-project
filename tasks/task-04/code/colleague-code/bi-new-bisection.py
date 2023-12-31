import numpy as np
from scipy.interpolate import lagrange
import random
from functions import find_initial_values, bisection

# Generate a random plaintext
plain_text = "Hello, World! This is a sample plaintext."

# Encode the plaintext using UTF-8 encoding
plain_bytes = plain_text.encode('utf-8')

# Convert the bytes to a list of integers representing the individual byte values
digits = list(plain_bytes)

# # Example usage:
# print("Plaintext:", plain_text)
# print("Plaintext blocks:", blocks)

# Randomly select an odd degree between 1 and 13
degree = random.choice(range(1, 14, 2))
# degree = 5

# x values for interpolation.
# Why she was starting from 1 not from 0?
x = list(range(0, degree + 1))

# y values for interpolation.
# What if the number of characters in the plain text is less
# than the degree of the polynomial?
y = digits[:degree+1]
# print(f"x values = {x} and y values = {y}")
poly = lagrange(x, y)  # the returned polynomial is a poly1d object

# Print the polynomial
print(f"Generated Polynomial: \n{poly}")

# Step 3: Generate scrambled polynomial
f = poly - digits  # Subtract x to obtain f(x) = poly - x
# print(f"The polynomia F = \n{f}")
poly_coefficients = f.coefficients  # Get the coefficients of f(x)

# Differentiate f(x) , The derivative of a polynomial represents the rate
# of change of the polynomial with respect to x. The resulting df represents
# the derivative of f(x).
df = np.polyder(f)
# Evaluate f(0) and take absolute value , Taking the absolute value ensures
# that the constant value is positive
constant = abs(f(0))

# Step 4: Guess initial values using find_initial_values function
method = 'bisection'
initial_values = find_initial_values(f, degree, method)

# Step 5: Apply the bisection method
error = 1e-6
root, fx, n, a, b = bisection(f, initial_values[0], initial_values[1], error)


print("Plain Text:", plain_text)
print("Degree of the polynomial:", degree)
print("Root value:", root)
print("Function value at root:", fx)
print("Number of iterations:", n)
print("Updated interval [a, b]:", [a, b])
