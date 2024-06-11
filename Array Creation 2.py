import numpy as np

'''make a array of all elements as 0'''
arr1=np.zeros([2,3])
print(arr1)

'''make a array of all elements as 1'''
arr2=np.ones((2,3))
print(arr2)

'''make a empty array --- it contains random elements'''
arr3=np.empty((3,4))
print(arr3)

'''make a empty array with dimensions similar to another array'''
arr4=np.empty_like(arr3)
print(arr4)

'''make a array for a given range'''
arr5=np.arange(1,11)   #makes 1-D array from number 1-10
print(arr5)
#with a jump
arr6=np.arange(1,11,3)
print(arr6)

'''make array with linear or equal spaces'''
arr7=np.linspace(1,10,5)  #make array of 5 elements equally dividing the range 1-10
print(arr7)

'''make a identity matrix'''
ide=np.identity(5)
print(ide)