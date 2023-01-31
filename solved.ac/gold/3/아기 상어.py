import sys,heapq
from collections import deque
readline = sys.stdin.readline

def bfs(x,y,shark):
    move = [(1,0),(-1,0),(0,1),(0,-1)]
    visited = [[0]*N for _ in range(N)]
    q = deque([(x,y)])
    food = []
    while q:
        x,y = q.popleft()
        for dx,dy in move:
            nx,ny= x+dx,y+dy
            if not (0 <= nx < N and 0 <= ny < N and board[ny][nx] <= shark and not visited[ny][nx]):
                continue
            q.append((nx,ny))
            visited[ny][nx] = visited[y][x] + 1
            if 0 < board[ny][nx] < shark: 
                heapq.heappush(food,(visited[ny][nx],ny,nx))
    return food[0] if food else None

N = int(readline())
board = [list()]*N
for y in range(N):
    board[y] = list(map(int,readline().split()))
    for x in range(N): 
        if board[y][x] == 9: 
            board[y][x] = 0
            sx,sy = (x,y)
res = 0
shark,exp = 2,0
find = bfs(sx,sy,shark)
while find:
    D,sy,sx = find
    board[sy][sx] = 0
    res += D
    exp += 1
    if exp == shark: shark,exp = shark+1,0
    find = bfs(sx,sy,shark)
print(res)