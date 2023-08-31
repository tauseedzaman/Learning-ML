# working matrix in numpy
import numpy as np

matrix = np.matrix([
    [1, 2, 9],
    [5, 6, 9],
])

print(matrix.reshape(3,2))

# print(matrix.reshape(2,3))

# print("matrix: \n", matrix)

# print("\nmatrix[0]:", matrix[0])
# print("\nmatrix[1]:", matrix[1])

# operations
# matrix_a = np.array([[1, 2], [3, 4]])
# matrix_b = np.array([[5, 6], [7, 8]])

# result = np.dot(matrix_a, matrix_b)

# print(result)
