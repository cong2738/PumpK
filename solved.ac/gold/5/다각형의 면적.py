import sys
from collections import defaultdict as dd
readline = sys.stdin.readline

def sizeof_cross_product(dot1,dot2,dot3):
    (x1,y1),(x2,y2),(x3,y3) = dot1,dot2,dot3
    return ((x1*y2 + x2*y3 + x3*y1) - (y1*x2 + y2*x3 + y3*x1)) / 2


N = int(readline())

dot = [tuple(map(int,readline().split())) for _ in range(N)]

res = 0
for i in range(1,N):
    res += sizeof_cross_product(dot[0],dot[i-1],dot[i])

print(abs(res))