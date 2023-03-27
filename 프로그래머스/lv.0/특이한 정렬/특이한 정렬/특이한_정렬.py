from math import gcd
def solution(a, b):
    answer = 0    
    g = gcd(a,b)    
    a=int(a/g)
    b=int(b/g)
    print(g,a,b)
    pr=2
    while(b>1):
        if b%pr==0:
            if pr!=5 and pr!=2 :
                return 2
            b = int(b/pr)
            pr=2
        else:
            pr+=1
    return 1
print(solution(11,22))