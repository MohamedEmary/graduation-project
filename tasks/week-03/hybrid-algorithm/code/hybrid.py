import sympy
import time


"""
Todo:
  - Return number of iterations and which method was applied
"""


def hybrid_root_finder(f, a, b, tol=10**(-10), max_iter=50):

    # False position attempts
    x0 = a
    x1 = b
    for i in range(max_iter):
        x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))

        if abs(f(x2)) < tol:
            return x2

        if f(x0)*f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

    # Bisection method
    while abs(b - a) > tol:
        c = (a + b) / 2

        if f(c) == 0 or abs(b - a) < tol:
            return c

        if f(a)*f(c) < 0:
            b = c
        else:
            a = c

    return "No root found"


# ================================

f = sympy.lambdify(sympy.Symbol('x'), 'x**3 + 4*x**2 - 10')

a = 0  # lower bound of the interval
b = 4  # upper bound of the interval

total_time = 0
num_runs = 500
iter = 0
for i in range(num_runs):
    start_time = time.time()
    result, iter = hybrid_root_finder(f, a, b)
    end_time = time.time()
    run_time = end_time - start_time
    total_time += run_time

average_time = total_time / num_runs

print(
    f"***Result over {num_runs} runs***\nAverage Time: {average_time}s \nIterations: {iter}\nRoot: {result}")


# ================================

"""
# ================================
f_str = input("Enter function f(x):")
f = sympy.lambdify(x, f_str)

a = float(input("Enter lower bound:"))

b = float(input("Enter upper bound:"))

tol = float(input("Enter tolerance:"))

max_iter = int(input("Enter max iterations for false position:"))

root = hybrid_root_finder(f, a, b, tol, max_iter)
print("Root: ", root)
# ================================
"""
