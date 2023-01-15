import sys
from collections import deque
readline = sys.stdin.readline

N = int(readline())
board = [[int(c) for c in readline().rstrip()] for _ in range(N)]
visited = [[False]*N for _ in range(N)]

def bfs(sx,sy):
    move = [(0,1),(1,0),(0,-1),(-1,0)]
    Q = deque( [(sx,sy)] )
    cnt = 0
    while Q:
        cnt += 1
        x,y = Q.popleft()
        board[y][x] = 0
        for dx,dy in move:
            nx,ny = x+dx,y+dy
            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx] and board[ny][nx]:
                visited[ny][nx] = True
                Q.append( (nx,ny) )
    return cnt

res = []
for x in range(N):
    for y in range(N):
        if board[y][x]: res.append(bfs(x,y))
print(len(res),*sorted(res),sep='\n')