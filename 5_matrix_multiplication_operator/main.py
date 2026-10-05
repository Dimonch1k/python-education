import numpy

A = numpy.array([[1, 2], [3, 4]])
B = numpy.array([[5, 6], [7, 8]])

C = A @ B
D = A * B

print("A:\n", A)
print("B:\n", B)
print("C = A @ B:\n", C)
print("D = A * B:\n", D)

# Alternatively, you can use the numpy.dot() function or the dot() method of the ndarray object to perform matrix multiplication:
# numpy.dot(A, B)
# A.dot(B)


# Performs matrix multiplication
C = A @ B

# Defines how an object behaves when it appears on the right side of @:
A.__matmul__(B)

# Handles matrix multiplication when the left operand doesn't handle the operation:
B.__rmatmul__(A)

# Supports the in-place form:
A @= B
