#changing the shape of the array
import numpy as np
rg=np.random.default_rng(1)
a=np.floor(10*rg.random((3,4)))
print(a)   #random numbers between 0 to 10
print(a.shape)

b=a.ravel()   #returns multidiemensional array into 1-D array
print(b)

c=b.reshape(2,6)  #change the shape of array
print(c)

d=c.T  #transpose of array
print(d)
print(d.shape)
print(d.T.shape)

a.resize(2,6)    #modifies the original array irrespective of the reshape function which just return an another array with change in its shape
print(a)

f=a.reshape(3,-1)   #if -1 arguement is given , it is automatically calculated
print(f)