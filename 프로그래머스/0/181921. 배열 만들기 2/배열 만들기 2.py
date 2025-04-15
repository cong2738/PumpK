def solution(l, r):
    res = sorted([i for i in range(l,r+1) if set(str(i)) == {'5','0'} or set(str(i)) == {'0'} or set(str(i)) == {'5'}])
    return res if res else [-1]