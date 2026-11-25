#SAME EXAMPLE
# Practice 5: compare Taylor approximation of sin(x) (Example 11)

import math
import numpy as np

def sin_taylor(x, n_terms):
    total = 0.0

    for k in range(n_terms):
        power = 2 * k + 1
        term = ((-1)**k) * x**power / math.factorial(power)
        total += term

    return total

x_values = [0.1, 0.5, 1.0, 2.0]

for x in x_values:
    print(f"\nx = {x} rad")

    for n in range(1, 6):
        approx = sin_taylor(x, n)
        absolute_error = abs(np.sin(x) - approx)

        print(
            f"Terms: {n}, "
            f"Approximation: {approx:.10f}, "
            f"Absolute error: {absolute_error:.3e}"
        )