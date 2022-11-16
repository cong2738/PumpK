
def cola(k):
    rt = [k]
    while k>1:
        if k%2==0:
            k/=2            
        else:
            k=k*3+1
        rt.append(int(k))
    return rt
def area(col):
    A=[]
    for x in range(len(col)-1):
        A.append((col[x]+col[x+1])/2)
    return A
def solution(k, ranges):
    answer = []
    Area = area(cola(k))
    for ra in ranges:
        tmp=0
        a=ra[0]
        b=len(Area)+ra[1]
        if a>b:
            tmp=-1
        else:
            for x in range(a,b):
                tmp+=Area[x]
        answer.append(tmp)
    return answer
