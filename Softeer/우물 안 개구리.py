import sys
readline = sys.stdin.readline

def around(p):
    for np in graph[p]: 
        if W[np] >= W[p]: return 0
    return 1

N,M = map(int, readline().split())
W = list(map(int,readline().split()))
graph = [[] for _ in range(N)]
for _ in range(M):
    A,B = map(lambda x:int(x)-1,readline().split())
    graph[A].append(B)
    graph[B].append(A)

res = sum([around(i) for i in range(N)])
print(res)