import numpy as np

a=np.arange(12).reshape(3,4)
b=a>4
print(b)

a[b]=0   #true value will change to 0
print(a)

#ix_()
b=np.array([2,3,4,5])
c=np.array([8,5,4])
d=np.array([5,4,6,8,3])
bx,cx,dx=np.ix_(b,c,d)
print(bx)
print(cx)
print(dx)
print(bx.shape,cx.shape,dx.shape)
result=bx+cx*dx
print(result)

#Vector stacking
x=np.arange(0,10,2)
y=np.arange(5)
m=np.vstack([x,y])
n=np.hstack([x,y])
print(m)
print(n)