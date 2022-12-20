import sys
input = sys.stdin.readline
from collections import deque
reg = [[]*10000]
def D(n): return str(2*int(n)%10000)
def S(n): return str(int(n)-1) if int(n) != 0 else str(9999)
def L(n): 
    if len(n) < 4: n = '0'*(4 - len(n)) + n
    tmp = deque(char for char in n)
    tmp.rotate(-1)
    return str(int(''.join(tmp)))
def R(n): 
    if len(n) < 4: n = '0'*(4 - len(n)) + n
    tmp = deque(char for char in n)
    tmp.rotate(1)
    return str(int(''.join(tmp)))
move = [D,S,L,R]

def find():
    origine, trans = input().split()
    tsQ = deque([[origine,'']])
    visited = {origine:''}
    while(True):
        while tsQ:
            bef = tsQ.popleft()            
            for cmd in move:
                data = [cmd(bef[0]), bef[1]+cmd.__name__]
                if data[0] == trans: return data[1]
                if not data[0] in visited:
                    visited[data[0]]=data[1]
                    tsQ.append(data)

T = int(input())
for tc in range(T):
    print(find())
