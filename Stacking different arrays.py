import numpy as np
rg=np.random.default_rng(1)
a=np.floor(10*rg.random((2,2)))
print(a)
b=np.floor(10*rg.random((2,2)))
print(b)

c=np.vstack((a,b))    #vertical stacki
print(c)

d=np.hstack((a,b))    #horizontal stack
print(d)

e=np.column_stack((a,b))   #returns a 2-D array
print(e)

a=np.array([2,3])
b=np.array([4,5])

f=np.column_stack((a,b))
print(f)

print(a[:,np.newaxis])  #return "a" as 2-D column vector
print(b[:,np.newaxis])  #returm "b" as 2-D column vector

print(np.column_stack((a[:,np.newaxis],b[:,np.newaxis])))
print(np.hstack((a[:,np.newaxis],b[:,np.newaxis])))

#NOTE--- column_stack and h_stack are not same whereas vstack and row_stack are same
print(np.column_stack is np.hstack)
print(np.row_stack is np.vstack)

print(np.r_[1:5,0,4])  #used for stacking numbers along one axis only
print(np.c_[5,3,1])