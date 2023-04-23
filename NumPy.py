import numpy as np

p = [[1, 2], [3, 4]]
q = [[5, 6], [7, 8]]

a = [1, 2, 3]
b = [0, 1, 0]


print(p)
print(q)
result = np.dot(p, q)
print(result)

result2 = np.outer(p, q)
print(result2)

result3 = np.einsum("mk,kn", p, q)
print(result3)

result4 = np.einsum("k,k", a, b)
print(result4)

determinant = np.linalg.det(p)
print(determinant)

sumofDiag = np.trace(p)
print(sumofDiag)

a = np.array([[1, 0, 0, 0, 2], [0, 0, 3, 0, 0],
             [0, 0, 0, 0, 0], [0, 2, 0, 0, 0]])

U, S, V = np.linalg.svd(a, full_matrices=False)
print(U)
print(S)
print(V)

b = np.arange(1, 10).reshape(3, 3)
norm = np.linalg.norm(b, 'fro')
cond = np.linalg.cond(b, 'fro')

print(norm)
print(cond)

c = np.arange(1, 10)
c = c[::-1]
print(c)

d = np.zeros((8, 8), dtype=int)
d[1::2, ::2] = 1
d[::2, 1::2] = 1
print(d)

print(np.asarray(p))

array1 = np.array([0, 10, 20, 40, 60, 80])
print("Array1: ", array1)
array2 = [10, 30, 40, 50, 70]
print("Array2: ", array2)
print("Unique values in array1 that are not in array2:")
print(np.setdiff1d(array1, array2))

f = np.zeros((5, 5))
f += np.arange(5)
print(f)
