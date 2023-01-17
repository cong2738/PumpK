import sys
from collections import deque
readline = sys.stdin.readline

def bfs(start,visited,color):
    move = [(0,1),(1,0),(0,-1),(-1,0)]
    Q = deque([start])
    while Q:
        x,y = Q.popleft()
        for dx,dy in move:
            nx,ny = x+dx,y+dy
            if not (0 <= nx < N and 0 <= ny < N and not visited[ny][nx] and board[ny][nx] in color): continue
            Q.append((nx,ny))
            visited[ny][nx] = True
    return 1

N = int(readline())
board = [readline().rstrip() for _ in range(N)]
res1,res2 = 0,0
visited1 = [[0]*N for _ in range(N)]
visited2 = [[0]*N for _ in range(N)]
for x in range(N):
    for y in range(N):
        if not visited1[y][x]: res1 += bfs((x,y),visited1,{board[y][x]})
        if not visited2[y][x]: res2 += bfs((x,y),visited2,{'B'} if board[y][x] == 'B' else {'R','G'})

print(res1,res2)