def solution(t, p):
    res = 0
    for i in range(len(t) - len(p) + 1):
        if int(t[i:i+len(p)]) <= int(p): res += 1
    return res