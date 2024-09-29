import sys
readline = sys.stdin.readline

dfs_result = []
def dfs(p):
    dfs_result.append(p)
    visited[p] = True
    for np in tree[p]:
        if not visited[np]: 
            dfs(np)

bfs_result = []
def bfs(p):
    visited[p] = True   
    q = [p]
    while q:
        p = q.pop()
        bfs_result.append(p)
        for np in tree[p]:
            if not visited[np]:
                q.append(np)
                visited[np] = True

def set_visited():
    return [False for _ in range(N+1)]

#main
N,M,V = map(int, readline().split())
tree = [[] for _ in range(N+1)]

for i in range(M):
    a,b = map(int, readline().split())
    tree[a].append(b)
    tree[b].append(a)

for i in range(N):
    tree[i+1].sort()


visited = set_visited()
dfs(V)
visited = set_visited()
bfs(V)
print(*dfs_result)
print(*bfs_result)