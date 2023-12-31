import numpy as np


def find_initial_values(f, degree, method):
    # Create a poly1d object from the polynomial coefficients
    poly = np.poly1d(f)  # f is a

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
