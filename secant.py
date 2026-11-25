#15 Secant Method

def secant(f, x0, x1, tolerance=1e-8, max_iter=100):
    errors = []

    for iteration in range(1, max_iter + 1):
        denominator = f(x1) - f(x0)

        if denominator == 0:
            raise ZeroDivisionError("Zero denominator.")

        x2 = x1 - f(x1) * (x1-x0) / denominator

        error = abs((x2-x1) / x2) * 100
        errors.append(error)

        if error < tolerance:
            return x2, iteration, errors

        x0 = x1
        x1 = x2

    return x1, max_iter, errors


def f(x):
    return x**3 - 4*x - 9


root, iterations, errors = secant(f, 2.0, 3.0)

print("Root =", root)
print("f(root) =", f(root))
print("Iterations =", iterations)
print("Final error (%) =", errors[-1])