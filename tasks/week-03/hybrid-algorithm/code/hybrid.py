import sympy

print("Enter function f(x):")
f_str = input()
f = sympy.lambdify(x, f_str)

print("Enter lower bound:")
a = float(input())

print("Enter upper bound:")
b = float(input())

print("Enter tolerance:")
tol = float(input())

print("Enter max iterations for false position:")
max_iter = int(input())


def hybrid_root_finder(f, a, b, tol, max_iter):

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

    return None


root = hybrid_root_finder(f, a, b, tol, max_iter)
print("Root: ", root)
