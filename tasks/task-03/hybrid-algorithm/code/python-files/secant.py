import math
import time


def secant(f, x0, x1, tol=(10**(-10)), max_iter=1000):
    # Initialize an iteration counter
    i = 0
    # Repeat until the tolerance is met or the maximum number of iterations is reached
    while abs(x1 - x0) > tol and i < max_iter:
        # Compute the function values at the current points
        f_x0 = f(x0)
        f_x1 = f(x1)
        # Calculate the new point using the secant method formula
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        # Update the points for the next iteration
        x0, x1 = x1, x2
        i += 1
    return x1, f(x1), i


def f(x):
    return x**4 - 8*x**3 + 18*x**2 - 9*x + 1


x0 = 2  # initial guess
x1 = 4  # another initial guess

total_time = 0
num_runs = 500
for i in range(num_runs):
    start_time = time.time()
    result, fx, iter = secant(f, x0, x1)
    end_time = time.time()
    run_time = end_time - start_time
    total_time += run_time

average_time = total_time / num_runs

print(f"Iterations: {iter}")
print(f"Average time: {average_time}s")
print(f"Root: {result}")
print(f"f(x): {fx}")
