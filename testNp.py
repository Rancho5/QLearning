
import numpy as np

# change array to matrix
array = np.array([[1,2,3],
                   [2,3,4]])


# attributes of numpy
# print(array)
# print('number of dim:',array.ndim)
# print('shape:',array.shape)
# print('size:',array.size)

# create matrix
a = np.array([1, 2, 3], dtype=int)
# print(a.dtype)
a0 = np.zeros((3, 4), dtype=int)
a1 = np.ones((3, 4), dtype=int)
a2 = np.arange(10, 20, 2)
a3 = np.arange(12).reshape((3, 4))
# print('a0:\n', a0)
# print('a1:', a1)
# print('a2:', a2)
# print('a3:', a3)

# Operations of Matrix
b1 = a3 ** 2;
b2 = a3 * np.sin(b1);
b3 = a3 * b1;
b4 = np.dot(a3, b1.reshape((4, 3)))
b5 = a3.dot(b1.reshape((4, 3)))
b6 = np.random.random((3, 4))
# print("a3\n", a3, "\nb\n", b1)
# print("b2\n", b2)
# print(a3 < 3)
# print("b3\n", b3)
# print("b4\n", b4)
# print("b5\n", b5)
# print("b6\n", b6)
# print(np.sum(b6, axis=0))
# print(np.min(b6, axis=1))
# print(np.max(b6, axis=0))

print("a3\n", a3)
print(np.argmax(a3))
print(np.mean(a3), a3.mean())
print(np.median(a3))
print("b6\n", b6)
print(np.sort(b6))
print(b6.T)     # transpose