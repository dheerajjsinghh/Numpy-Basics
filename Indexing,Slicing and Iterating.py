#Indexing ,Slicinng and Iterating
import numpy as np

#1-D array
a=np.arange(10)**3   #prints cube till number 9
print(a)
print(a[4:8])  #prints elements from 4 to 7

a[:8:2]=1000  #change elemets at gap of 2 into 1000 till the range of 8
print(a)
print(a[::-1])     #reverse the string
for x in a:
    print(x**(1/3))   #print square root of all digits of the array

#multidimensional array
def f(x,y):
    return 10*x +y
b=np.fromfunction(f,(5,4))
print(b)

print(b[2,3])   #row 2 and column 3
print(b[0:5,2])   #row 0 to 4 and column 2
print(b[0:5,1:3])
print(b[-1])   #last row ...equivalent to b[-1,:]
for element in b.flat:
    print(element,end=" ")
for row in b:
    print(row)
#3-D array
c=np.array([[[0,1,2],[10,12,13]],[[100,101,102],[110,112,113]]])
print(c.shape)
print(c[1,...])   #equivalent to c[1,:,:]
print(c[...,2])  #equivalent to c[:,:,2]
for x in c:
    print(x)
for y in c.flat:
    print(y)
d=c.ravel()    #converts multidimensionl array to 1-D array
print(d)
