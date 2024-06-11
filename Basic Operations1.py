import numpy as np
arr1=np.array([0.1,0.2,0.3])
arr2=np.array([[0,1,2,3,4,5],[1,2,3,4,5,6]])

'''determine the shape and size of the array'''
print(arr1.shape)
print(arr2.shape)

print(arr1.size)
print(arr2.size)

'''number of dimensions of the array'''
print(arr1.ndim)
print(arr2.ndim)

'''data type of array'''
print(arr1.dtype)
print(arr2.dtype)

'''size of particular element of array'''
print(arr1.itemsize)
print(arr2.itemsize)

'''total number of bytes taken bya an array'''
print(arr1.nbytes)
print(arr2.nbytes)

