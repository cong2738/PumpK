import sys
readline = sys.stdin.readline

def find_startpoint():
    for y in range(H):
        for x in range(W):
            if board[y][x] != '#': continue
            count = 0
            for i,(dx,dy) in enumerate(around):
                nx,ny = x+dx,y+dy
                if 0 <= nx < W and 0 <= ny < H and board[ny][nx] == '#':
                    count += 1
                    ahead = i
            if count == 1: 
                board[y][x] = '.'
                return (x,y,ahead)

around = ((0,1),(1,0),(0,-1),(-1,0))
ahead_char = ('v','>','^','<')
H,W = map(int,readline().split())
board = [list(readline().rstrip()) for _ in range(H)]
x,y,ahead = find_startpoint()
print(f'{y+1} {x+1}\n{ahead_char[ahead]}')
res = ''
while True:
    for i,(dx,dy) in enumerate(around):
        nx,ny = x+2*dx,y+2*dy
        if not (0 <= nx < W and 0 <= ny < H and board[y+dy][x+dx] == '#'): continue
        board[y+dy][x+dx] = '.'
        board[y+2*dy][x+2*dx] = '.'
        if ahead == i: res += 'A'
        elif (ahead+1)%4 == i: res += 'LA'
        else: res += 'RA'
        x,y,ahead = nx,ny,i
        break
    else: break
print(res)