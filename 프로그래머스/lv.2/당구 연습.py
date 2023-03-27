def length(p1,p2,lx,ly):
    col = lambda x : (2*(x[0]**2) + (x[1]**2) + (x[2]**2))
    
    tmp = list()

    (x1,y1),(x2,y2) = p1,p2
    if not (x1 == x2 and y1 > y2):
        tmp.append((abs(x1-x2)/2, y1, y2))
    if not (x1 == x2 and y1 < y2):
        tmp.append((abs(x1-x2)/2, ly-y1, ly-y2))
    if not (y1 == y2 and x1 > x2):
        tmp.append((abs(y1-y2)/2, x1, x2))
    if not (y1 == y2 and x1 < x2):
        tmp.append((abs(y1-y2)/2, lx-x1, lx-x2))
    print(list(map(col,tmp)))
    return min(map(col,tmp))

def solution(m, n, startX, startY, balls):
    answer = [length((startX,startY),(x,y),m,n) for x,y in balls]
    return answer

print(length((3,7),(7,3),10,10))