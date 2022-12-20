import sys
readline = sys.stdin.readline

np = [[0,1],[0,-1],[1,0],[-1,0]]

def bfs(graph,x,y):
    queue = [[x,y]]
    graph[y][x] = 0
    while queue:
        x,y = queue.pop(0)
        for dx,dy in np:
            nx,ny = x+dx,y+dy
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
                graph[ny][nx] = 0
                queue.append([nx,ny])

for _ in range(int(readline())):
    worm_count = 0
    m,n,k = map(int,readline().split())
    field = [[0]*m for _ in range(n)]
    
    for _ in range(k):
        x,y = map(int,readline().split())
        field[y][x] = 1
    
    for y in range(n):
        for x in range(m):
            if field[y][x]:
                bfs(field,x,y)
                worm_count += 1

    print(worm_count)
