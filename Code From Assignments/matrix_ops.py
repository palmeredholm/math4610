from vectors import dot_prod


def mat_add(A, B):
    # Check to see if matrices are conformable
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise Exception('Matrices are non-conformable')
    # Create matrix for addition of values
    C = [[0 for i in range(len(A))] for j in range(len(A))]
    # Traverse the two matrices and update the C matrix with the sum of the elements
    for i in range(len(C)):
        for j in range(len(C)):
            C[i][j] = A[i][j] + B[i][j]
    # Return the matrix addition of A and B
    return C


def mat_subtract(A, B):
    # Check to see if matrices are conformable
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise Exception('Matrices are non-conformable')
    # Create matrix for addition of values
    C = [[0 for i in range(len(A))] for j in range(len(A))]
    # Traverse the two matrices and update the C matrix with the subtraction of the elements
    for i in range(len(C)):
        for j in range(len(C)):
            C[i][j] = A[i][j] - B[i][j]
    # Return the matrix subtraction of A and B
    return C


def mat_scalar(a, A):
    return [[a * A[i][j] for j in range(len(A[i]))] for i in range(len(A))]


def transpose(A):
    # Return the transpose of the given matrix A
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


def mat_vec_prod(A, x):
    # Check to see if this matrix and vector are conformable
    if (not isinstance(A[0], list)) or (len(A[0]) != len(x)) or (len(A) <= 1) or (isinstance(x[0], list)):
        raise Exception('Non-conformable')
    # Initialize empty resultant vector
    B = [0 for i in range(len(A))]
    # Sum the respective products
    for i in range(len(A)):
        el = 0
        for j in range(len(x)):
            el += float(A[i][j]) * float(x[j])
        B[i] = el
    # Return resultant vector
    return B


def mat_prod(A, B):
    # Check to see that the matrices are conformable
    if (not isinstance(A[0], list)) or (len(A[0]) != len(B)) or (not isinstance(B[0], list)):
        raise Exception('Non-conformable')
    # Initialize empty matrix for resultant dot product
    C = [[0 for i in range(len(A))] for j in range(len(A))]
    # Traverse both matrices and append resulting dot product to C
    for i in range(len(A)):
        for j in range(len(A)):
            C[i][j] = dot_prod(A[i], [row[j] for row in B])
    # Return resultant matrix
    return C
