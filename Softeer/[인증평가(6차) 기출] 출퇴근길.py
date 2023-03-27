import sys
from collections import deque
readline = sys.stdin.readline

def input():
    n,m = map(int,readline().split())
    graph = {i:set() for i in range(1,n+1)}
    for _ in range(m):
        a,b = map(int,readline().split())
        graph[a].add(b)
    S,T = map(int,readline().split())

    return n,m,graph,S,T

def dfs(start,end,graph):
    ret = {start,end}    
    Q = deque([(start,{start,end})])
    while Q:
        p,way = Q.pop()
        for np in graph[p]:
            if np in ret:
                ret |= way
                continue
            Q.append((np,way|{np}))

n,m,graph,S,T = input()

