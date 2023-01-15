import sys
readline = sys.stdin.readline

def slice(board,x,y,dx,dy):
    return [line[x:x+dx] for line in board[y:y+dy]]

def all_good(photo):
    color = photo[0][0]
    for line in photo:
        for pixel in line:
            if pixel != color: return -1
    return color

def rcs(photo):
    flag = all_good(photo)
    if flag != -1: return flag
    ret = list()
    sizeDiv2 = len(photo)//2
    for i in range(2):
        for j in range(2):
            ret.append((rcs(slice(photo,j*sizeDiv2,i*sizeDiv2,sizeDiv2,sizeDiv2))))
    return tuple(ret)

photo = [list(map(int,readline().rstrip())) for _ in range(int(readline()))]
res = rcs(photo)
print(str(res).replace(', ',''))