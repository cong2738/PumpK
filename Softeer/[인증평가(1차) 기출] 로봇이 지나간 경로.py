import sys
readline = sys.stdin.readline
around = ((0,1),(1,0),(0,-1),(-1,0))
ahead_char = ('v','>','^','<')

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
            
def robomove(x,y,ahead):
    ret = ''
    while True:
        for i,(dx,dy) in enumerate(around):
            nx,ny = x+2*dx,y+2*dy
            if 0 <= nx < W and 0 <= ny < H and board[y+dy][x+dx] == '#':
                if ahead == i: ret += 'A'
                elif (ahead+1)%4 == i: ret += 'LA'
                else: ret += 'RA'
                board[y+dy][x+dx] = '.'
                board[y+2*dy][x+2*dx] = '.'
                x,y,ahead = nx,ny,i
                break
        else: return ret

H,W = map(int,readline().split())
board = [list(readline().rstrip()) for _ in range(H)]
sx,sy,ahead = find_startpoint()
print(f'{sy+1} {sx+1}\n{ahead_char[ahead]}\n{robomove(sx,sy,ahead)}')