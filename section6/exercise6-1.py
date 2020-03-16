import numpy as np


def gaussian_Elim(A, v):
    '''
    solves the system of equations associated with the matrix A and vector v
    :param A: square matrix
    :param v: vector
    :return: vector containing the solutions to the system of eqns
    '''
    N = len(v)
    # Gaussian Elimination
    for m in range(N):
        # Partial pivoting
        largest = abs(A[m, m])
        largest_row = m
        for i in range(m + 1, N):
            if abs(A[i, m]) > largest:
                largest = abs(A[i, m])
                largest_row = i
        if largest_row != m:
            # switch rows in A
            current_row = np.copy(A[m, :])  # need to use copy because A[m, :] is a reference
            A[m, :] = A[largest_row, :]
            A[largest_row, :] = current_row

            # switch rows in v
            v[m], v[largest_row] = v[largest_row], v[m]

        # Divide by the diagonal element
        div = A[m,m]
        A[m, :] /= div
        v[m] /= div

        # Now subtract from the lower rows
        for i in range(m + 1, N):
            mult = A[i, m]
            A[i, :] -= mult * A[m, :]
            v[i] -= mult * v[m]

    # Backsubstitution
    x = np.empty(N, float)
    for m in range(N-1, -1, -1):
        x[m] = v[m]
        for i in range(m+1, N):
            x[m] -= A[m, i] * x[i]

    return x

A = np.array([[4 ,-1, -1, -1],
        [1, -3, 0, 1],
        [-1, 0, 3, -1],
        [1, 1, 1, -4]], float)
v = np.array([5, 0, 5, 0], float)

print(gaussian_Elim(A,v))

