import sympy
import time


def bisection(f, a, b, tol=(10**(-10))):
    # Check if a and b bracket a root
    if f(a) * f(b) > 0:
        return 'No root found in the interval', 'No root found in the interval'
    # Initialize x as the midpoint of a and b
    x = (a + b) / 2
    # Initialize an iteration counter
    i = 1
    # Repeat until the interval is smaller than the tolerance
    while abs(b - a) > tol:
        # If x is a root, return it
        if f(x) == 0:
            return x, i
        # If f(a) and f(x) have opposite signs, set b = x
        elif f(a) * f(x) < 0:
            b = x
        # If f(b) and f(x) have opposite signs, set a = x
        else:
            a = x
        # Update x as the new midpoint of a and b
        x = (a + b) / 2
        i += 1
    return x, i


x = sympy.Symbol('x')
func = x**3 + 4*x**2 - 10
f = sympy.lambdify(x, sympy.sympify(func))

a = 0       # lower bound of the interval
b = 4       # upper bound of the interval

total_time = 0
num_runs = 500
iter = 0
for i in range(num_runs):
    start_time = time.time()
    result, iter = bisection(f, a, b)
    end_time = time.time()
    run_time = end_time - start_time
    total_time += run_time

average_time = total_time / num_runs

print(
    f"***Result over {num_runs} runs***\nAverage Time: {average_time}s \nIterations: {iter}\nRoot: {result}")
