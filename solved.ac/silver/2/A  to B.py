import sys
from collections import deque as dq
readline = sys.stdin.readline

def bfs(start,end) -> int:
    Q = dq([(start,1)])
    while Q:
        p,cnt = Q.popleft()
        if p == end: return cnt
        for np in (2*p, 10*p + 1):
            if np > end: continue
            Q.append((np,cnt+1))

    return -1

print(bfs(*map(int,readline().split())))