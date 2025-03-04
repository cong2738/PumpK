import sys
from collections import deque
readline = sys.stdin.readline

H,W = map(int,readline().split())
pic = [list(map(int,readline().split())) for _ in range(H)]

def bfs(sx,sy,K):
    sx-=1; sy-=1
    if pic[sy][sx] == K: return []
    move = [(0,1),(0,-1),(1,0),(-1,0)]
    visited = [[False]*W for _ in range(H)]
    color = pic[sy][sx]
    Q = deque([(sx,sy)])
    while Q:
        x,y = Q.popleft()
        pic[y][x] = K
        for dx,dy in move:
            nx,ny = x+dx,y+dy
            if not (0 <= nx < W and 0 <= ny < H and pic[ny][nx] == color and not visited[ny][nx]): continue
            visited[ny][nx] = True
            Q.append((nx,ny))

for _ in range(int(readline())):
    y,x,K = map(int,readline().split())
    bfs(x,y,K)

print(*[' '.join(map(str,line)) for line in pic],sep='\n')