import sys
from collections import deque
readline = sys.stdin.readline
around = ((0,1),(1,0),(-1,0),(0,-1))
def findstart():
    for y in range(H):
        for x in range(W):
            if board[y][x] != '#': continue
            count = 0
            for i,(dx,dy) in enumerate(around):
                nx,ny = x+dx,y+dy
                if 0 <= nx < W and 0 <= ny < H and board[ny][nx] == '#':
                    count += 1
                    ahead = i
            if count == 1: return (x,y,ahead)
H,W = map(int,readline().split())
board = [list(readline().rstrip()) for _ in range(H)]
visited = [[False]*W for _ in range(H)]
start = findstart()
board[start[1]][start[0]] = '.'
ahead_char = {(0,1):'v',(1,0):'>',(0,-1):'^',(-1,0):'<'}
res = ''
Q = deque([start])
while True:
    x,y,ahead = Q.popleft()
    dx, dy = around[ahead]*2, around[ahead]*2
    nx,ny = x+2*dx,y+2*dy
    if 0 <= nx < W and 0 <= ny < H and board[ny][nx] == '#':            
        res += 'A'
        board[ny][nx] = '.'
        board[ny-dy][nx-dx] = '.'
        Q.append((nx,ny,ahead))
    else:
        flag1,flag2 = ahead[0]-dx,ahead[1]-dy
        if ahead[0] == 0:
            res += 'R' if flag1==flag2 else 'L'
        elif ahead[1] == 0:
            res += 'L' if flag1==flag2 else 'R'
        ahead = (dx,dy)

print(start[1]+1,start[0]+1)
print(ahead_char[start[2]])
print(res)