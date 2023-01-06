import sys
readline = sys.stdin.readline
W,N = map(int,readline().split())
jewels = sorted([list(map(int,readline().split())) for _ in range(N)],key=lambda x:x[1],reverse=True)
res = 0
for m,p in jewels:
    if W <= m: 
        res += p*W
        break
    else: 
        res += m*p
        W -= m
print(res)