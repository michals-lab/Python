import numpy as nu

x = nu.arange(9).reshape(3,3)
y = nu.arange(16).reshape(4,4)
print(x)
print(y)
a=[]
b=[]
c=[]
d=[]
for i in range(3):
    a.append(nu.min(x[:,i]))
    b.append(nu.min(x[i,:]))

for i in range(4):
    c.append(nu.min(y[:,i]))
    d.append(nu.min(y[i,:])) 

print(a)
print(b)
print(c)
print(d)