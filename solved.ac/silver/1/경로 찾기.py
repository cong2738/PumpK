import sys
from collections import deque
readline = sys.stdin.readline

def bfs(start,visited):
    Q = deque([start])
    while Q:
        p = Q.popleft()
        for np in range(len(visited)):
            if not graph[p][np] or visited[np]: continue
            visited[np] = 1
            Q.append(np)
    return visited

N = int(readline())
graph = [list(map(int,readline().split())) for i in range(N)]
v = [[0]*(N) for _ in range(N)]
for i in range(N): print(*bfs(i,v[i]))