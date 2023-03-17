import sys,heapq
def dijkstra(graph, start):
    dis = {node:0 for node in graph}
    #dis[start] = 0
    q = [(dis[start],start)]
    while q:
        d, p = heapq.heappop(q)
        if dis[p] < d: continue
        for np in graph[p]:
            nd = max(d,graph[p][np])
            if nd > dis[np]:
                dis[np] = nd
                heapq.heappush(q,(nd,np))
    print(dis)
    return
from collections import defaultdict as dd
readline = sys.stdin.readline
N,M = map(int,readline().split())
visited = [False] * N
graph = dd(dict)
for _ in range(M):
    a,b,c = map(int,readline().split())
    graph[a][b] = min(c,graph[a][b]) if b in graph[a] else c
    graph[b][a] = min(c,graph[a][b]) if b in graph[a] else c

print(dijkstra(graph,1))