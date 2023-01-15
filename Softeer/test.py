import sys
move = [(0,1),(1,0),(0,-1),(-1,0)]
x = 1
y = 2
INF = [(x+move[i][0],y+move[i][1]) for i in range(4)]
print(INF)