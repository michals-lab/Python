import numpy as nu
def fib(n):
    wynik = [1,1]
    for i in range(n-2):
        wynik.append(wynik[i] + wynik[(i+1)])
    return wynik

x = nu.array(fib(25)).reshape(5,5)
print(x)