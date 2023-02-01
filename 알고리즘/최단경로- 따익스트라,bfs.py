from math import inf
import sys, heapq

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


# 다익스트라 최적경로 탐색
def dijkstra(graph, start):
    distances = [inf] * (V+1)
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        recent_dist, recent_node = heapq.heappop(queue)

        # 기존 최단거리보다 멀다면 무시
        if distances[recent_node] < recent_dist:
            continue

        # 노드와 연결된 인접노드 탐색
        for next_node, next_distance in graph[recent_node]:
            distance = recent_dist + next_distance
            # 기존 거리 보다 짧으면 갱신
            if distance < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(queue, [distance, next_node])
    return distances

res = dijkstra(graph, K)
for i in range(1, V+1):
    print("INF" if res[i] == inf else res[i])