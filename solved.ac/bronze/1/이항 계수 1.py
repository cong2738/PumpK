import math
fac = math.factorial
n,k = map(int,input().split())
if 0 <= k <= n: print(int(fac(n)/(fac(k)*fac(n-k))))
else: print(0)