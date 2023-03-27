def find_S(park):
    for y,line in enumerate(park):
        for x,c in enumerate(line):
            if c == 'S': return x,y
    return None

def solution(park, routes):
    dir_char = {'E':(1,0),'W':(-1,0),'S':(0,1),'N':(1,0)}
    LX,LY = len(park[0]),len(park)
    x,y = find_S(park)    
    nx,ny = x,y
    for cmd in routes:
        dir,dis = (lambda x:(x[0],int(x[1])))(cmd.split())
        dx,dy = dir_char[dir]
        for i in range(1,dis+1):
            nx,ny = x+dx,y+dy
            if not (0 <= nx < LX and 0 <= ny < LY and park[ny][nx] == 'O'): break
        else: 
            x,y = nx,ny
        print(x,y)
            
    return [y,x]