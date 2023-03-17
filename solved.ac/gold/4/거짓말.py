import sys
from collections import deque
readline = sys.stdin.readline

def bfs(start):
    Q = deque([start])
    while Q:
        p = Q.popleft()
        for np in graph[p]:
            if np in know: continue
            know.add(np)
            Q.append(np)

N,M = map(int,readline().split())
Tn,*T = map(int,readline().split())
know = set(T)

graph = {p:set() for p in range(1,N+1)}
party_time = []
for _ in range(M):
    pn,*party = list(map(int,readline().split()))
    party_time.append(set(party))
    for i in party:
        graph[i] |= set(party)

for p in T: bfs(p)

res = 0
for party in party_time:
    if party & know: continue
    res += 1

print(res)
    