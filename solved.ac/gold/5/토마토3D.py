import sys
nxt = [[1,0,0],[-1,0,0],[0,-1,0],[0,1,0],[0,0,1],[0,0,-1]]
n,m,h=map(int,sys.stdin.readline().split())
tmt_box, red_loc = [[list(map(int, sys.stdin.readline().split())) for _ in range(m)] for _ in range(h)], list()
green, red, date = 0, 0, 0
for z in range(h):
    for y in range(m):
        for x in range(n):
            if tmt_box[z][y][x] == 0:
                green += 1
            elif tmt_box[z][y][x] == 1:
                red_loc.append([x,y,z])
while red_loc:        
    new_red = []
    for x,y,z in red_loc:
        for dx,dy,dz in nxt:
            nx, ny, nz = x+dx, y+dy, z+dz 
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and tmt_box[nz][ny][nx] == 0:                
                    tmt_box[nz][ny][nx] = 1
                    new_red.append([nx,ny,nz])
                    green-=1    
    red_loc = new_red
    date+=1
print(date-1 if green == 0 else -1)