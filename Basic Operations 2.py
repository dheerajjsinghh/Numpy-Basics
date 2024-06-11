import numpy as np
a=np.arange(30,40,3)
print(a)
b=np.arange(4)
print(b)

'''addition and subtraction'''
c=a+b
print(c)
c=a-b
print(c)

'''exponent'''
print(b**2)

'''sin/cos'''
print(np.sin(a))
print(np.cos(b))

'''condition'''
print(b>1)

'''product'''
A=np.array([[2,3],[4,5]])
B=np.array([[6,7],[8,9]])
print(A*B)   # element wise product
print(A@B)   #matrix product
print(A.dot(B))  #matrix product

'''random number'''
rg=np.random.default_rng(1)
D=np.ones((2,3))
C=rg.random((2,3))
print(C)
print(C+D)

'''random complex number'''
print(np.exp(c*1j))

'''mathematical tools'''
print(C.sum())   #sum of all elements of array
print(C.max())   #max number out of all elements of array
print(C.min())   #min number out of all elements of array
print(A.cumsum())
print(C.cumsum())  #print cumulative sum

'''operations across axis'''
print(C.sum(axis=0))   #sum of matrix in a vertical manner
print(C.sum(axis=1))   #sum of matrix in horizontal manner
print(C.min(axis=0))
print(C.sum(axis=1))
print(C.cumsum(axis=0))
print(C.cumsum(axis=1))