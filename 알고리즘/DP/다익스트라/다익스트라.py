import sys,heapq,math
#다익스트라 최단 경로 탐색 레퍼런스 *중복방문 허용
N,graph = int(1),dict() #N은 노드갯수, graph는 Dictionaly형태의 연결리스트 ex> {node1:{node2:distance}}
def dijkstra(s,e):
    dis = {n:math.inf for n in range(1,N+1)} #거리를 저장할 데이터시트 최초값은 조혼나 큰 수
    dis[s] = 0
    q = [(0,s)]
    while q:
        d,p = heapq.heappop(q)
        if d > dis[p]:continue
        for np in graph[p]:
            if dis[np] <= dis[p] + graph[p][np]: continue
            dis[np] = dis[p] + graph[p][np]
            heapq.heappush(q,(dis[np],np))
    return dis[e] #타겟까지의 최단거리(없다면 조혼나 큰수 반환)