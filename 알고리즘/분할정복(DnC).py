def DnC(a,b,c):
    if b==1:
        return a%c
    temp = DnC(a,b//2,c)
    temp *= temp
    if b%2 != 0: temp *= a
    return temp%c

a,b,c = map(int,input().split())        
ans = DnC(a,b,c)
print(ans)