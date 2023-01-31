import sys,heapq
from collections import deque
readline = sys.stdin.readline
N = int(readline())
board = [list()]*N
for y in range(N):
    board[y] = list(map(int,readline().split()))
    for x in range(N): 
        if board[y][x] == 9: 
            sx,sy = (x,y)

def bfs(x,y,shark):
    move = [(1,0),(-1,0),(0,1),(0,-1)]
    visited = [[0]*N for _ in range(N)]
    q = deque([(x,y)])
    foodloc = []
    while q:
        x,y = q.popleft()
        for dx,dy in move:
            nx,ny= x+dx,y+dy
            if not (0 <= nx < N and 0 <= ny < N and not visited[ny][nx]):
                continue
            q.append((nx,ny))
            visited[ny][nx] = visited[y][x] + 1
            if 0 < board[ny][nx] <= shark: 
                heapq.heappush(foodloc,(visited[ny][nx],ny,nx))
    return foodloc

res = 0
shark = 1
find = bfs(sx,sy,shark)
while find:
    D,sy,sx = find[0]
    res += D
    if board[sy][sx] == shark: shark += 1
    board[sy][sx] = 0
    find = bfs(sx,sy,shark)
print(res)