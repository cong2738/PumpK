
nxt = [[1,0],[-1,0],[0,-1],[0,1]]
n,m=map(int,input().split())
tmt_box, red_loc = [list(map(int, input().split())) for _ in range(m)], list()
green, red, date = 0, 0, 0
for y in range(m):    
    for x in range(n):
        if tmt_box[y][x] == 0:
            green += 1
        elif tmt_box[y][x] == 1:
            red_loc.append([x,y])
while red_loc:        
    new_red = []
    for x,y in red_loc:
        for dx,dy in nxt:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and tmt_box[ny][nx] == 0:                
                    tmt_box[ny][nx] = 1
                    new_red.append([nx,ny])
                    green-=1    
    red_loc = new_red
    date+=1
print(date-1 if green == 0 else -1)