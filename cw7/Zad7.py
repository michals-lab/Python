import numpy as nu
x = nu.arange(6).reshape(2,3)
print(x)
a = nu.sin(x)
print(a)
y = nu.arange(6).reshape(2,3)
print(y)
b = nu.cos(y)
print(b)
print(a+b)