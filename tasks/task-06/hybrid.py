from decimal import Decimal


class BiNew(object):
    def __init__(self, text, x, y):
        if type(text) != str or len(x) != len(y):
            raise ValueError("Invalid parameters passed")
        self.text = text
        self.len_text = len(text)
        self.x = [Decimal(i) for i in x]
        self.y = [Decimal(i) for i in y]
        self.coefs = None
        self.maximium_8utf_chars = Decimal(2122219134)
        self.minimum_8utf_chars = Decimal(538976288)
        self.len_x = len(x)

    def evaluate_interpolated_value(self, target, normalized_value=Decimal(0)):
        n = self.len_x
        result = Decimal(self.coefs[-1])
        for i in range(n - 2, -1, -1):
            result = Decimal(result) * \
                (Decimal(target) - Decimal(self.x[i])) + Decimal(self.coefs[i])
        return result - normalized_value

    def bisection_method(self, a, b, normalized_value, tol=Decimal(10 ** -38)):
        if self.evaluate_interpolated_value(a, normalized_value) * self.evaluate_interpolated_value(b, normalized_value) > 0:
            raise ValueError(
                "The function values at the endpoints must have different signs.")
        for i in range(40):
            midpoint = (a + b) / Decimal(2)
            if self.evaluate_interpolated_value(midpoint, normalized_value) == Decimal(0):
                return midpoint
            elif self.evaluate_interpolated_value(midpoint, normalized_value) * self.evaluate_interpolated_value(a, normalized_value) < 0:
                b = midpoint
            else:
                a = midpoint
        return midpoint

    def find_roots_secant(self, x0, x1, normalized_value, tol=Decimal(10 ** -17), max_iter=16):
        x_prev = Decimal(x0)
        x_curr = Decimal(x1)
        for i in range(max_iter):
            fx_prev = self.evaluate_interpolated_value(
                x_prev, normalized_value)
            fx_curr = self.evaluate_interpolated_value(
                x_curr, normalized_value)
            if fx_curr - fx_prev == 0:
                raise ValueError(
                    "Secant method cannot converge. Division by zero.")
            x_next = x_curr - fx_curr * (x_curr - x_prev) / (fx_curr - fx_prev)
            x_prev = x_curr
            x_curr = x_next
            if abs(fx_curr) < tol:
                return x_curr
        return x_curr

    def hybrid_bisection_secant(self, a, b, x0, x1, normalized_value, tol=Decimal(10 ** -17), max_iter=16):
        # Bisection
        if self.evaluate_interpolated_value(a, normalized_value) * self.evaluate_interpolated_value(b, normalized_value) > 0:
            raise ValueError(
                "The function values at the endpoints must have different signs.")
        # Secant
        x_prev = Decimal(x0)
        x_curr = Decimal(x1)
        while (True):
            # Bisection
            midpoint = (a + b) / Decimal(2)
            fx_mid = self.evaluate_interpolated_value(
                midpoint, normalized_value)
            if fx_mid == Decimal(0):
                return midpoint
            elif fx_mid * self.evaluate_interpolated_value(a, normalized_value) < 0:
                b = midpoint
            else:
                a = midpoint
            # Secant
            fx_prev = self.evaluate_interpolated_value(
                x_prev, normalized_value)
            fx_curr = self.evaluate_interpolated_value(
                x_curr, normalized_value)
            if fx_curr - fx_prev == 0:
                raise ValueError(
                    "Secant method cannot converge. Division by zero.")
            x_next = x_curr - fx_curr * (x_curr - x_prev) / (fx_curr - fx_prev)
            x_prev = x_curr
            x_curr = x_next
            # Return the closest to zero
            if (abs(fx_curr) or abs(fx_mid)) < tol:
                return x_curr if abs(fx_curr) < abs(fx_mid) else midpoint
