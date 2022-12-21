from math import factorial as fac
num = str(fac(int(input())))
L = len(num)
for i in range(L):
    if int(num[L-1-i]):
        print(i)
        break