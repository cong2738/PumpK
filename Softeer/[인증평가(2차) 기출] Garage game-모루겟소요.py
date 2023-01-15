import sys
from collections import deque
readline = sys.stdin.readline

N = int(readline())
zero = [deque() for _ in range(N)]
tower = [deque() for _ in range(N)]
for _ in range(2*N):
    for i,n in enumerate(map(int,readline().split())):
        tower[i].appendleft(n)
for _ in range(N):
    for i,n in enumerate(map(int,readline().split())):
        zero[i].appendleft(n)

visited = [[0]*N for _ in range(N)]
def bfs(start:tuple):
    if zero[start[1]][start[0]] != -1 and visited[start[1]][start[0]]: return {}
    ret = {start}
    color = zero[start[1]][start[0]]
    move = [(0,1),(1,0),(0,-1),(-1,0)]
    Q = deque([start])    
    while Q:
        x,y = Q.popleft()
        print(f'({x},{y})')
        for nx,ny in [(x+move[i][0],y+move[i][1]) for i in range(4)]:
            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx] and zero[ny][nx] == color:
                visited[ny][nx] = True
                Q.append((nx,ny))
                ret.add((nx,ny))
    print()
    return ret

popping = []
for x in range(N):
    for y in range(N):
        temp = bfs((x,y))
        if len(temp) <= 1: continue
        popping.append(temp)