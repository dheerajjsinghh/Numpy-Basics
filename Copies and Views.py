import numpy as np
a=np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])
print(a)

#NO COPY
b=a     #no new object is created
print(b is a)   #b and a are same object with different names
print(id(a),id(b))   #same

#VIEW OR SHALLOW COPY
c=a.view()
print(c)
print(c is a)
print(c.base is a)   #c is view of data owned by a .... it is not same object as a
print(c.flags.owndata)

c=c.reshape(2,6)
print(c)
c[0,3]=1245  #change value at given index
print(c)

d=a[:,1:3]   #d is same object as a for a particular range provided
print(d)
d[:]=10  # changes in d is equal  to changes in a
print(a)


#DEEP COPY
e=a.copy()   #now e and a are different objects with same value
#changes in e will not affect a
print(e is a)
e[0,0]=1234
print(e)
print(a)