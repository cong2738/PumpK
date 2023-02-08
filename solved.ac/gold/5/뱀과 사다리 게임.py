from collections import deque
import sys
readline = sys.stdin.readline
N,M = map(int,readline().split())
LS = dict()
for _ in range(N+M):
    s,e = map(int,readline().split())
    LS[s] = e
Q = deque([1])
visited = {1:0}
while Q:
    p = Q.popleft()
    if p == 100: break
    for dice in range(1,6+1):
        np = LS[p+dice] if p+dice in LS else p+dice
        if np > 100 or np in visited: continue
        Q.append(np)
        visited[np] = visited[p]+1
print(visited[100])