from collections import defaultdict as dd
import sys
readline = sys.stdin.readline

# input param
T = int(readline())
for _ in range(T):
    N,K = map(int,readline().split())
    D = list(map(int,readline().split()))
    req = dd(set)
    for _ in range(K):
        x,y = map(int,readline().split())
        req[y].add(x)
    W = int(readline())
    print(*req.items(),sep = '\n')

# sol
