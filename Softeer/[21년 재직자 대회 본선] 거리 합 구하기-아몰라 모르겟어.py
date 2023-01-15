import sys
from math import inf
sys.setrecursionlimit(100000)
readline = sys.stdin.readline

def Floyd_Warshall():
    dist = [[inf]*N for i in range(N)] # 최단 경로를 담는 배열
    for i in range(N): # 최단 경로를 담는 배열 초기화
        for j in range(N):
            dist[i][j] = graph[i][j]
    for k in range(N): # 거치는 점
        for i in range(N): # 시작점
            for j in range(N): # 끝점
                # k를 거쳤을 때의 경로가 더 적은 경로
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

N = int(readline())
graph = [[inf]*(N) for _ in range(N+1)]
for i in range(N):
    graph[i][i] = 0
for i in range(N-1):
    p,c,d = map(int,readline().split())
    graph[p-1][c-1] = d
    graph[c-1][p-1] = d
dist = Floyd_Warshall()
print(*[sum(l) for l in dist],sep='\n')
    