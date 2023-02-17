import sys
readline = sys.stdin.readline
signal = [
    ((-1,0),((0,1),(0,-1),(1,0))),
    ((0,1),((-1,0),(0,-1),(1,0))),
    ((1,0),((0,1),(-1,0),(0,-1))),
    ((0,-1),((0,1),(-1,0),(1,0))),
    
    ((-1,0),((0,-1),(1,0))),
    ((0,1),((-1,0),(0,-1))),
    ((1,0),((0,1),(-1,0))),
    ((0,-1),((0,1),(1,0))),
    
    ((-1,0),((0,1),(1,0))),
    ((0,1),((0,-1),(1,0))),
    ((1,0),((-1,0),(0,-1))),
    ((0,-1),((0,1),(-1,0)))
]

def dfs(x,y,Time,bx,by):
    global N,T, board, signal, res
    rot,sig = signal[board[y][x][Time%4]-1] 
    if Time == T+1: return
    res.add((x,y))
    if (x+rot[0],y+rot[1]) == (bx,by):
        for dx,dy in sig:
            nx,ny = x+dx,y+dy
            if 0 <= nx < N and 0 <= ny < N: 
                dfs(nx,ny,Time+1,x,y)

res = set()
N,T = map(int,readline().split())
board = [[tuple(map(int,readline().split())) for x in range(N)] for y in range(N)]        
dfs(0,0,0,0,1)
print(len(res))