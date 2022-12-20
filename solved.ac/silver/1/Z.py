N,r,c = map(int,input().split())
ret = 0
while N != 0:
    N -= 1
    p2n = 2**N
    if r < p2n and c < p2n: pass
    elif r < p2n and c >= p2n:
        ret += (p2n**2)*1
        c -= p2n
    elif r >= p2n and c < p2n:
        ret += (p2n**2)*2
        r -= p2n
    else: 
        ret += (p2n**2)*3
        r -= p2n
        c -= p2n
print(ret)