def binpow(C,n):
    if n == 1:
        ret = C
    else:
        x = binpow(C,n//2)
        if n % 2 == 0:
            ret = x*x
        else:
            ret = x*x*C
    return ret %1000000007
K,P,N = map(int,input().split())
print(K*binpow(P,N*10)%1000000007)