from collections import defaultdict as dd

def check_req(target:dd,req:dd):
    for key in req.keys():
        if target[key] - req[key] < 0: break
    else: 
        return 1

    return 0

S,P = map(int,input().split())
DNA = input()
req = dict(zip(['A','C','G','T'],map(int,input().split())))

res = 0
cnt = dd(int)
for i in range(P): cnt[DNA[i]] += 1

res += check_req(cnt,req)

start,next = 0,P
while next < S:    
    cnt[DNA[start]] -= 1
    cnt[DNA[next]] += 1    
    res += check_req(cnt,req)
    start+=1
    next += 1

print(res)