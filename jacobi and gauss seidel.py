import numpy as np
import matplotlib.pyplot as plt

def jacobi(A, b, tol=1e-10, max_iter=100):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    x = np.zeros(len(b))
    errors = []

    for _ in range(max_iter):
        x_new = np.zeros_like(x)

        for i in range(len(b)):
            s = np.dot(A[i, :], x) - A[i, i] * x[i]
            x_new[i] = (b[i] - s) / A[i, i]

        error = np.linalg.norm(x_new - x, np.inf)
        errors.append(error)
        x = x_new

        if error < tol:
            break

    return x, errors

def gauss_seidel(A, b, tol=1e-10, max_iter=100):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    x = np.zeros(len(b))
    errors = []

    for _ in range(max_iter):
        x_old = x.copy()

        for i in range(len(b)):
            s = np.dot(A[i, :], x) - A[i, i] * x[i]
            x[i] = (b[i] - s) / A[i, i]

        error = np.linalg.norm(x - x_old, np.inf)
        errors.append(error)

        if error < tol:
            break

    return x, errors

A = np.array([
    [10.0, 2.0, 1.0],
    [1.0, 5.0, 1.0],
    [2.0, 3.0, 10.0]
])

b = np.array([7.0, -8.0, 6.0])

x_j, e_j = jacobi(A, b)
x_g, e_g = gauss_seidel(A, b)

print("Jacobi:", x_j)
print("Jacobi iterations:", len(e_j))

print("\nGauss-Seidel:", x_g)
print("Gauss-Seidel iterations:", len(e_g))

plt.semilogy(range(1, len(e_j) + 1), e_j,
             marker="o", label="Jacobi")
plt.semilogy(range(1, len(e_g) + 1), e_g,
             marker="s", label="Gauss-Seidel")

plt.xlabel("Iteration")
plt.ylabel("Infinity-norm change")
plt.title("Iterative Method Convergence")
plt.grid(True)
plt.legend()
plt.show()
