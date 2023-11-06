import math
import time


def falsePosition(f, x0, x1, e=(10**(-10))):
    step = 1
    condition = True
    while condition:
        x2 = x0 - (x1-x0) * f(x0)/(f(x1) - f(x0))
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        step += 1
        condition = abs(f(x2)) > e

    return x2, f(x2), step, x0, x1


def f(x): return x**4 - 8*x**3 + 18*x**2 - 9*x + 1


x0 = 2  # lower bound of the interval
x1 = 4  # upper bound of the interval

total_time = 0
num_runs = 500
iter = 0
for i in range(num_runs):
    start_time = time.time()
    result, fx, iter, x0, x1 = falsePosition(f, x0, x1)
    end_time = time.time()
    run_time = end_time - start_time
    total_time += run_time

average_time = total_time / num_runs

print(f"Iterations: {iter}")
print(f"Average time: {average_time}s")
print(f"a: {x0}")
print(f"Root: {result}")
print(f"b: {x1}")
print(f"f(x): {fx}")
