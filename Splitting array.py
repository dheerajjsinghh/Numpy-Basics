import numpy as np
rg=np.random.default_rng(1)
a=np.floor(10*rg.random((2,12)))
print(a)

c=np.hsplit(a,3)
print(c)
d=np.hsplit(a,(3,4))
print(d)

b=a.reshape(12,2)
print(b)

e=np.vsplit(b,3)
print(e)
f=np.vsplit(b,(4,3))
print(f)