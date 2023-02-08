import sys,heapq
readline = sys.stdin.readline
#다익스트라
def dijkstra(s,e):
    dis = {n:float('inf') for n in range(1,N+1)}
    dis[s] = 0
    q = [(0,s)]
    while q:
        d,p = heapq.heappop(q)
        if d > dis[p]:continue
        for np in graph[p]:
            nd = d+graph[p][np]
            if dis[np] <= nd: continue
            dis[np] = nd
            heapq.heappush(q,(nd,np))
    return dis[e]

N,E = map(int,readline().split())
graph = {n:dict() for n in range(1,N+1)}
#해당 그래프는 모두 양방향.
for _ in range(E):
    a,b,c = map(int,readline().split())
    graph[a][b] = c
    graph[b][a] = c
v1,v2 = map(int,readline().split())
#이미 이동한 정점,간선도 이동할 수 있다는 조건이 존재, 다익스트라 중복 사용 최단거리 추론.
#{1 - v1 - v2 - N}, {1 - v2 - v1 - N}의 두가지 경로.
s_to_v1 = dijkstra(1,v1)
s_to_v2 = dijkstra(1,v2)
v1_to_v2 = dijkstra(v1,v2)
v1_to_e = dijkstra(v1,N)
v2_to_e = dijkstra(v2,N)
path = min(s_to_v1+v2_to_e, s_to_v2+v1_to_e) + v1_to_v2
print(path if path != float('inf') else -1)