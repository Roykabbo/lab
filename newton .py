#12: Newton Raphson

def newton_raphson(f, df, x0, tolerance=1e-8, max_iter=100):
    errors = []
    x = x0

    for iteration in range(1, max_iter + 1):
        derivative = df(x)

        if derivative == 0:
            raise ZeroDivisionError("Derivative is zero.")

        x_new = x - f(x) / derivative

        error = abs((x_new - x) / x_new) * 100
        errors.append(error)

        if error < tolerance:
            return x_new, iteration, errors

        x = x_new

    return x, max_iter, errors


def f(x):
    return x**3 - 4*x - 9

def df(x):
    return 3*x**2 - 4


root, iterations, errors = newton_raphson(f, df, 3.0)

print("Root =", root)
print("f(root) =", f(root))
print("Iterations =", iterations)
print("Final error (%) =", errors[-1])