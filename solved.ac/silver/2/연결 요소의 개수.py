import sys
readline = sys.stdin.readline

n,m = map(int,readline().split())
visited = [True] + [False for _ in range(n)]
graph = dict()
for _ in range(m):
    a,b = map(int,readline().split())
    if a in graph: graph[a].add(b)
    else: graph[a] = {b}
    if b in graph: graph[b].add(a)
    else: graph[b] = {a}
#dfs
sys.setrecursionlimit(1000000)
def dfs(parent):
    global visited, graph, cnt
    visited[parent] = True
    if not parent in graph: return
    for child in graph[parent]:
        if not visited[child]: dfs(child)  

def Connected_Component():
    cnt = 0
    while True:
        for i in range(1,n+1):
            if not visited[i]: 
                cnt += 1
                dfs(i)
                break
        else: break
    return cnt         
print(Connected_Component())
