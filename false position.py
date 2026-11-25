#9 Full False Position


def false_position(f, xl, xu, tolerance=1e-8, max_iter=100):
    if f(xl) * f(xu) > 0:
        raise ValueError("Interval does not bracket a root.")

    errors = []
    xr_old = None

    for iteration in range(1, max_iter + 1):
        denominator = f(xl) - f(xu)

        if denominator == 0:
            raise ZeroDivisionError("Zero denominator.")

        xr = xu - f(xu) * (xl - xu) / denominator

        if xr_old is not None:
            error = abs((xr - xr_old) / xr) * 100
            errors.append(error)

            if error < tolerance:
                return xr, iteration, errors

        if f(xl) * f(xr) < 0:
            xu = xr
        elif f(xl) * f(xr) > 0:
            xl = xr
        else:
            return xr, iteration, errors

        xr_old = xr

    return xr, max_iter, errors



def f(x):
    return x**3 - 4*x - 9


root, iterations, errors = false_position(f, 2.0, 3.0)

print("Root =", root)
print("f(root) =", f(root))
print("Iterations =", iterations)
print("Final error (%) =", errors[-1] if errors else 0.0)