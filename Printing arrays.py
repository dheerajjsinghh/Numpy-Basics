import numpy as np
arr1=np.arange(6)
print(arr1)

arr2=np.arange(12).reshape(3,4)  #changing the shape of 1-D array to 2-D array
print(arr2)

arr3=np.arange(24).reshape(2,3,4)
print(arr3)

'''if we have a very large range... Numpy itself skips the middle part and shows corners'''
arr4=np.arange(10000).reshape((100,100))
print(arr4)

