import numpy as np
import random


def vec_add(x, y):
    # Check to see if vectors are conformable
    if len(x) != len(y):
        raise Exception('Non-conformable arrays')
    # Return the element-wise addition of the two vectors
    return [x[i] + y[i] for i in range(len(x))]


def vec_subtract(x, y):
    # Check to see if vectors are conformable
    if len(x) != len(y):
        raise Exception('Non-conformable arrays')
    # Return the element-wise subtraction of the two vectors
    return [x[i] - y[i] for i in range(len(x))]


def vec_scalar(a, x):
    # Return the vector x where each element is scaled by the scalar a
    return [a * x[i] for i in range(len(x))]


def dot_prod(x, y):
    # Check to see if vectors are conformable
    if len(x) != len(y):
        raise Exception('Non-conformable arrays')
    # Initialize a sum variable
    dot = 0
    # Traverse each element in either array and sum the product of the respective elements
    for i in range(len(x)):
        dot += float(x[i]) * float(y[i])
    # Return the dot product of the two vectors
    return dot


def out_prod(x, y):
    # Check to see if vectors are conformable
    if len(x) != len(y):
        raise Exception('Non-conformable arrays')
    # Initialize matrix to fill with the elements of the outer product of x and y
    out = [[0 for i in range(len(x))] for j in range(len(x))]
    # Traverse the elements of each vector and create the respective element of the outer product
    for i in range(len(x)):
        for j in range(len(x)):
            out[i][j] = float(x[i]) * float(y[j])
    # Return outer product matrix
    return out
