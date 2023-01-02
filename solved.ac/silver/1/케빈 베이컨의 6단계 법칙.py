from collections import deque
import sys

readline = sys.stdin.readline
N,M = map(int,readline().split())
graph = {a:set() for a in range(1,N+1)}
for _ in range(M):
    a,b = map(int,readline().split())
    graph[a].add(b); graph[b].add(a)

def bfs(visited,start):
    dq = deque([start])
    while dq:
        p = dq.popleft()
        for np in graph[p]:
            if not visited[np] and np != start:
                visited[np] = visited[p] + 1
                dq.append(np)
    return sum(visited)

bacon = {start:bfs([0 for _ in range(N+1)],start) for start in range(1,N+1)}
print(min(bacon.items(),key=lambda x:x[1])[0])