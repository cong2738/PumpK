def solution(dots):
    dydx = []
    for i in range(-1,len(dots)-1):
        dydx.append((dots[i][1]-dots[i+1][1])/(dots[i][0]-dots[i+1][0]))
    for i in dydx:
        if 1 < dydx.count(i):
            return 1
    return 0