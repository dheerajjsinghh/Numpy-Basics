import numpy as np
a=np.arange(12)**2
i=np.array([1,1,3,8,5])  #array consisting of index values of a
print(a[i])
j=np.array([[3,4],[9,7]])
print(a[j])

#
time=np.linspace(20,145,5)
data=np.sin(np.arange(20)).reshape(5,4)
print(time)
print(data)

#index of maxima of each series
ind=data.argmax(axis=0)
print(ind)

#times corresponding to maxima
time_max=time[ind]
print(time_max)

data_max=data[ind,range(data.shape[1])]
print(data_max)

print(np.all(data_max==data.max(axis=0)))


#advanced value assign
a=np.arange(5)
print(a)
a[[0,0,2]]=[1,2,3]
print(a)