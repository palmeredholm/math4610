def diagsub(A, b):
    # Initialize vector of unknowns and variable for loops
    x = []
    n = len(b)
    # compute values of unknowns
    for i in range(n):
        x.append(b[i] / A[i, i])
    # Return the solution of the system
    return x
