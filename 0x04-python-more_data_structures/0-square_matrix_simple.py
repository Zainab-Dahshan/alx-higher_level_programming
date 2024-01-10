#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same dimensions as the input matrix
    result = [[0]*len(row) for row in matrix]

    # Iterate over each element in the input matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Square the value and store it in the corresponding position in the result matrix
            result[i][j] = matrix[i][j] ** 2
    return (result)
