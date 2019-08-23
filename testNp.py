
import numpy as np

# change array to matrix
array = np.array([[1,2,3],
                   [2,3,4]])


#attributes of numpy
print(array)
print('number of dim:',array.ndim)
print('shape:',array.shape)
print('size:',array.size)

#create matrix
a = np.array([1, 2, 3], dtype=int)
print(a.dtype)
a0 = np.zeros((3, 4), dtype=int)
a1 = np.ones((3, 4), dtype=int)
a2 = np.arange(10, 20, 2)
a3 = np.arange(12).reshape((3, 4))
print('a0:\n', a0)
print('a1:', a1)
print('a2:', a2)
print('a3:', a3)
