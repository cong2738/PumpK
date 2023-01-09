#분할정복을 사용한 거듭제곱
import sys
K,P,N = map(int,sys.stdin.readline().split())
def binpow(c,n):
    res = 1
    while n:
        if n & 1:
            res *= c
        c *= c
        n >>= 1
    return res
print(K * binpow(P,N) % 1000000007)