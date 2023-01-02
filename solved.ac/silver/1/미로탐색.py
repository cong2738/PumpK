import sys
from collections import deque
readline = sys.stdin.readline
N,M = map(int,readline().split())
maze = [list(map(int,readline().rstrip())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
def bfs():
    moves = [[0,1],[1,0],[0,-1],[-1,0]]
    dq =  deque([(0,0)])
    visited[0][0] = 1
    while dq:
        x,y = dq.popleft()
        if x+1 == M and y+1 == N: return 'Find'
        for dx,dy in moves:
            nx,ny = x+dx,y+dy
            if 0 <= nx < M and 0 <= ny < N and maze[ny][nx] and not visited[ny][nx]:                
                visited[ny][nx] = visited[y][x] + 1
                dq.append((nx,ny))             
    return 'None'
bfs()
print(visited[N-1][M-1])
