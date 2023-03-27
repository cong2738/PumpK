from audioop import maxpp
from gettext import find
from itertools import combinations
def solution(lines):
    combi = list(combinations(lines,2))
    cross = []
    xx=[]
    yy=[]
    for p in combi:
        A,B,E = p[0]
        C,D,F = p[1]
        ADmBC = A*D-B*C
        if ADmBC != 0:
            x = ((B*F-E*D)/ADmBC)
            y = ((E*C-A*F)/ADmBC)
            if (x - int(x) == 0) and (y - int(y) == 0):
                xx.append(x)
                yy.append(y)
                cross.append([x, y])
    list.sort(xx)
    list.sort(yy)
    paint = []
    for i in range(int(yy[0]),int(yy[-1])+1):
        L=""
        for j in range(int(xx[0]), int(xx[-1])+1):
            if [j,i] in cross:
                L+='*'
            else:
                L+='.'
        paint.append(L)
    paint.reverse()
    return paint

lines = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]	
for x in solution(lines):
    print(x)