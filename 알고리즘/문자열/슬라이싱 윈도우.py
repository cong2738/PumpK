'''
슬라이싱 윈도우
 공통요소 수 비교에 유용한 알고리즘
 이미 저장된 데이터에서 사라질 데이터를 지우고 새 데이터를 받는식으로
 기존 데이터를 최대한 활용하여 불필요한 반복연산을 줄인다. O(n)
 #기차가 이동하며 역에 도착하고 짐을 내리고 싣는 모습을 생각하면 이해하기 쉽다.

-----------------------------------------------------------
data    |123456|            | res
-----------------------------------------------------------
0.      |123   | 1,2,3 in   | {1:1,2:2,3:3}     sum = 6
1.      | 234  | 4 in 1 out | {1:0,2:1,3:1,4:1} sum = 9
2.      |  345 | 5 in 2 out | {2:0,3:1,4:1,5:1} sum = 12
3.      |   456| 6 in 3 out | {3:0,4:1,5:1,6:1} sum = 15
-----------------------------------------------------------
'''
from collections import defaultdict as dd

data = ['A','C','G','T']

def check_req(target:dd,req:dd):
    for key in data:
        if target[key] - req[key] < 0:  return 0
        
    return 1

def run():
    S,P = map(int,input().split())
    DNA = input()
    req = dict(zip(data,map(int,input().split())))

    cnt = dd(int)
    for i in range(P): cnt[DNA[i]] += 1

    res = check_req(cnt,req)
    start,next = 0,P
    while next < S:    
        cnt[DNA[start]] -= 1
        cnt[DNA[next]] += 1    
        res += check_req(cnt,req)
        start+=1
        next += 1
    
    print(res)
    

if __name__ == '__main__': run()