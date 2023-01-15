import sys
readline = sys.stdin.readline

res = 0
N,K = map(int,readline().split())
coins = list(reversed([int(readline()) for _ in range(N)]))
for coin in coins:
    res += K // coin
    K %= coin
    if K == 0: break
print(res)