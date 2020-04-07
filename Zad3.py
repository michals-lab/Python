import sys
with open("liczby2.txt","w") as x:
    for i in range(0,51):
        x.write(str(i)+"\n")
with open("liczby2.txt","r") as x:
    for i in x:
        print(i, end="")