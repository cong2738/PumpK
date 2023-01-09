import sys
from collections import deque
readline = sys.stdin.readline

N = int(readline())
board = [list(map(int,list(readline().rstrip()))) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
move = [[0,1],[0,-1],[1,0],[-1,0]]
def bfs(sx,sy):
    visited[sy][sx] = True
    pset = set()
    q = deque([[sx,sy]])
    while q:        
        x,y = q.popleft()
        pset.add((x,y))
        board[y][x] = 0
        for dx,dy in move:
            nx,ny = x+dx,y+dy
            if 0<=nx<N and 0<=ny<N and board[ny][nx] and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append([nx,ny])
    return len(pset)

res = list()
block = 0
for y in range(N):
    for x in range(N):
        if board[y][x]:
            
            block_cnt = bfs(x,y)
            if block_cnt:
                block += 1
                res.append(block_cnt)
print(block,*sorted(res),sep='\n')