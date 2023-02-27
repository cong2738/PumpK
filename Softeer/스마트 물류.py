import sys
from collections import deque as dq
readline = sys.stdin.readline

def comp(target,stack,res,index,TD):
    if stack and abs(stack[0]-index) <= TD:
        res.append(stack[0])
        stack.popleft()
    else:
        if target and abs(target[0]-index) >= K: target.popleft()
        target.append(index)
    return target,stack,res

N,K = map(int,readline().split())
res,storage,robo = [],dq([]),dq([])
for i,c in enumerate(readline().rstrip()):
    if c == 'H':
        storage,robo,res = comp(storage,robo,res,i,K)
    elif c == 'P':
        robo,storage,res = comp(robo,storage,res,i,K)
print(len(res))