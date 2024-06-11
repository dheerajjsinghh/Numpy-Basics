import numpy as np

arr1=np.array([1,2,3,4])  #1-D array  with int datatype
print(arr1)
print(arr1.dtype)

arr2=np.array([[1.2,2.3,3.1,4.2],[5.5,6.3,7.2,8.5]])    #2-D array  with float datatype
print(arr2)
print(arr2.dtype)

arr3=np.array([[1,2],[3,4]],dtype=complex)  #array of complex number
print(arr3)
print(arr3.dtype)
