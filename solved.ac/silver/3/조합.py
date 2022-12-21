from math import factorial as fac
n,m = map(int, input().split())
nCm = fac(n)//(fac(n-m)*fac(m))
print(nCm)