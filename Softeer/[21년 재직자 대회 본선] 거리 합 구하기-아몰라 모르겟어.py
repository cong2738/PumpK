import sys,heapq as hq
readline = sys.stdin.readline

def dijkstra(graph, s):
    distances = {node:float('inf') for node in graph}
    distances[s] = 0
    HQ = []
    hq.heappush(HQ,[distances[s],s])
    while HQ:
        d, p = hq.heappop(HQ)
        if distances[p] < d: continue
        for np in graph[p]:
            distance = d + graph[p][np]
            if distance < distances[np]:
                distances[np] = distance
                hq.heappush(HQ,[distance,np])
    return distances
    
N =int(readline())
graph = {node:dict() for node in range(1,N+1)}
for _ in range(N-1):
    a,b,d = map(int,readline().split())
    graph[a][b] = d
    graph[b][a] = d
for i in range(1,N+1):
    s = 0
    for d in dijkstra(graph,i).values():
        if d == float('inf'): continue
        s += d
    print(s)

