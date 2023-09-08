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

stack = deque([])
visited = list()
def dfs(dir,p,E):
    global res,graph, visited, stack
    visited[p] = True
    stack.append(p)

    if p == E:
        #print(stack)
        for n in stack:
            if n in res[dir]: continue
            res[dir].add(n)
        stack.pop()
        return
    
    for np in graph[p]:
        if np in res[dir]: res[dir].add(p)
        if visited[np]: continue
        dfs(dir,np,E)
        visited[np] = False

    stack.pop()

def start_dfs(res,Start,End):
    global stack, visited
    stack = deque([])
    visited = [0]*(n+1)
    dfs(res,Start,End)

n,m,graph,S,T = input()

res = [set(),set()]

start_dfs(0,S,T)

start_dfs(1,T,S)

print(len(res[0] & res[1] - {S,T}))