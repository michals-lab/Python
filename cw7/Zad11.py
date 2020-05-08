import numpy as nu
x = nu.arange(12).reshape(1,12)
print(x)
a=x.reshape(3,4)
b=x.reshape(2,6)
c=x.reshape(4,3)
print(a.flat)
print(b.flat)
print(c.flat)