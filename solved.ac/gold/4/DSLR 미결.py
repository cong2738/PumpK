import sys
readline = sys.stdin.readline
from collections import deque

def D(n): return (2*n)%10000
def S(n): 
    return (n-1)%10000
def L(n):     
    front = n % 1000
    back = n // 1000
    return front*10 + back
def R(n): 
    front = n % 10
    back = n // 10
    return front * 1000 + back
move = [(D,'D'),(S,'S'),(L,'L'),(R,'R')]

def find(origine, trans):    
    tsQ = deque([(origine,'')])
    visited = {origine}
    while tsQ:
        num, res = tsQ.popleft()
        if num == trans: return res
        for op,name in move:
            nxtNum = op(num)
            if not nxtNum in visited:
                visited.add(nxtNum)
                tsQ.append((nxtNum, res + name))

for _ in range(int(readline())):
    origine, trans = map(int,readline().split())
    print(find(origine, trans))
