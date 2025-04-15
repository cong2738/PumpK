def solution(l, r):
    res = sorted([i for i in range(l,r+1) if not set(str(i)) - {'5','0'}])
    return res if res else [-1]