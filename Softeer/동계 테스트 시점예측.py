import sys
from collections import deque as dq
readline = sys.stdin.readline

N,M = map(int,readline().split())
board = [list(map(int,readline().split())) for y in range(N)]
def bfs():
    얼음 = False
    move = ((0,1),(0,-1),(1,0),(-1,0))
    C_board = [[0]*M for y in range(N)]
    visited = [[0]*M for y in range(N)]
    visited[0][0] = True
    Q = dq([(0,0)])
    while Q:
        x,y = Q.popleft()
        for dx,dy in move:
            nx,ny = x+dx,y+dy
            if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx]:
                if board[ny][nx]: 
                    얼음 = True
                    C_board[ny][nx] += 1
                    if C_board[ny][nx] >= 2: 
                        board[ny][nx] = 0
                        visited[ny][nx] = True
                else:
                    visited[ny][nx] = True
                    Q.append((nx,ny))
    return 얼음

cnt = 0
while(bfs()): cnt+=1
print(cnt)