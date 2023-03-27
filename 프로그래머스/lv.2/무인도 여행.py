from collections import deque

def bfs(sx:int,sy:int,maps:list[list[int]],visited:list[list[bool]]):
    ret = 0
    visited[sy][sx] = True
    move = [(1,0),(-1,0),(0,1),(0,-1)]
    Q = deque([(sx,sy)])
    while Q:
        x,y = Q.pop()
        ret += int(maps[y][x])
        for dx,dy in move:
            nx,ny = x+dx,y+dy
            if (not(0 <= nx < len(visited[0]) and 0 <= ny < len(visited)) 
                or maps[ny][nx] == 'X'
                or visited[ny][nx] ): 
                continue
            visited[ny][nx] = True
            Q.append((nx,ny))
    return ret

def solution(maps:list[list[int]]):
    answer = []
    visited = [[False]*len(maps[0]) for _ in range(len(maps))]
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if visited[y][x] or maps[y][x] == 'X': continue
            answer.append(bfs(x,y,maps,visited))
    return sorted(answer) if answer else [-1]

maps = ["X591X",
        "X1X5X",
        "X231X", 
        "1XXX1"]
print(solution(maps))