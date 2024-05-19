import time
import math


def FalseSecant(f, a, b, eps):
    n = 0

    while True:
        n += 1

        fa = f(a)
        fb = f(b)

        x_val = a - (fa * (b - a)) / (fb - fa)
        fx = f(x_val)

        if abs(fx) <= eps:
            return x_val, fx, n, a, b
        else:
            aS = b
            bS = x_val

            faS = fb
            fbS = fx

            xS = bS - fbS * (bS - aS) / (fbS - faS)
            fxS = f(xS)

            if abs(fxS) < abs(fx) and a < xS < b:
                if fa * fxS < 0:
                    b = xS
                else:
                    a = xS
            else:
                if fa * fx < 0:
                    b = x_val
                else:
                    a = x_val

# Define the function f(x)


def f(x):
    return x**4 - 8*x**3 + 18*x**2 - 9*x + 1


# Define the interval [a, b] and the tolerance eps
a = 2
b = 4
eps = 1e-10


total_time = 0
num_runs = 500
iter = 0
for i in range(num_runs):
    start_time = time.time()
    root, fx_val, iterations, a_final, b_final = FalseSecant(f, a, b, eps)
    end_time = time.time()
    run_time = end_time - start_time
    total_time += run_time

average_time = total_time / num_runs


print(f"Iterations: {iterations}")
print(f"Average time: {average_time}s")
print(f"Approximate Root: {root}")
print(f"Function Value at Root: {fx_val}")
print(f"Final Interval: [{a_final}, {b_final}]")
