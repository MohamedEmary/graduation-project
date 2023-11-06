import math
import time

# Define the function that implements the hybrid algorithm


def blendBF(f, a, b, eps=10**(-10)):
    # Initialize the variables
    n = 0
    a1 = a
    a2 = a
    b1 = b
    b2 = b

    while True:
        # Increment the iteration counter
        n += 1
        # Evaluate the function at the endpoints
        fa = f(a)
        fb = f(b)

        # Compute the midpoint and the false position point
        xB = (a + b) / 2
        fxB = f(xB)

        xF = a - (fa * (b - a)) / (fb - fa)
        fxF = f(xF)

        # Choose the one with the smaller absolute value as the root approximation
        if abs(fxB) < abs(fxF):
            x = xB
            fx = fxB
        else:
            x = xF
            fx = fxF

        # Check if the absolute value of fx is less than or equal to the tolerance
        if abs(fx) <= eps:
            # Return the output
            return x, fx, n, a, b

        # Update the interval by applying the bisection and false position methods
        if fa * fxB < 0:
            b1 = xB
        else:
            a1 = xB

        if fa * fxF < 0:
            b2 = xF
        else:
            a2 = xF

        # Set a to the maximum of a1 and a2 and b to the minimum of b1 and b2
        a = max(a1, a2)
        b = min(b1, b2)


# Example usage:
# Define function f(x) as a lambda function
def f(x): return x**4 - 8*x**3 + 18*x**2 - 9*x + 1


# Set the initial interval [a, b]
a = 2
b = 4


total_time = 0
num_runs = 500
iter = 0
for i in range(num_runs):
    start_time = time.time()
    x, fx, n, a_final, b_final = blendBF(f, a, b)
    end_time = time.time()
    run_time = end_time - start_time
    total_time += run_time

average_time = total_time / num_runs

print(f"Iterations: {n}")
print(f"Average time: {average_time}s")
print(f"a: {a_final}")
print(f"Root: {x}")
print(f"b: {b_final}")
print(f"f(x): {fx}")
