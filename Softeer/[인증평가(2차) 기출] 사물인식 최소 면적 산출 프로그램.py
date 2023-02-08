import sys
from itertools import combinations
readline = sys.stdin.readline
sys.setrecursionlimit(100000)
res = float('inf')
#첫번째 색(1)의 임의의 점하나를 시작으로 다음 색의 모든 점에대해 탐색하며 모든 색을 가진 크기가 (K)인 그룹을 만든경우 직사각형의 넓이를 확인한다. 모든 점에대해 반복한다
def dfs(mx,my,Mx,My,color,current):
    global res
    if color == K:
        res = current
        return
    next_color = color + 1
    for x,y in dots[next_color]:
        x1, x2, y1, y2 = min(mx,x), max(Mx,x), min(my,y), max(My,y)
        temp = abs(x1-x2)*abs(y1-y2)
        if temp >= res: continue
        dfs(x1,y1,x2,y2,next_color,temp)

N,K = map(int,readline().split())
dots = {color:[] for color in range(1,K+1)}
for i in range(N):
    x,y,color = map(int,readline().split())
    dots[color].append((x,y))
#첫번째 색의 모든 점에대해 탐색을 실시한다
for sx,sy in dots[1]: dfs(sx,sy,sx,sy,1,0)
print(res)