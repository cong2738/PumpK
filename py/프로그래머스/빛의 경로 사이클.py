def solution(grid):
    res = []
    N,M = len(grid),len(grid[0])
    moves = [(0,-1),(1,0),(0,1),(-1,0)]
    visited = [[[False] * 4 for _ in range(M)] for _ in range(N)]
    for y in range(N):
        for x in range(M):
            for d in range(4):
                if visited[y][x][d]: continue                
                nx,ny = x,y
                count = 0
                while not visited[ny][nx][d]:
                    dx,dy = moves[d]
                    visited[ny][nx][d] = True
                    count += 1
                    if grid[ny][nx] == 'L': d = (d-1)%4
                    elif grid[ny][nx] == 'R': d = (d+1)%4
                    nx = (x+dx)%M
                    ny = (y+dy)%N
                    res.append(count)
    return sorted(res)

print(*solution(["SL","LR"]))