import math
kat = [0, 30, 45, 60, 90]
sin = []
cos = []

for i in range (len(kat)):
    sin.append(math.sin(kat[i]))
    cos.append(math.cos(kat[i]))

print(sin)
print(cos)

