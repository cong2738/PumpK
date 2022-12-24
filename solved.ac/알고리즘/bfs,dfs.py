graph = dict()
visited = list()

dfsret = []
def dfs(p):
    dfsret.append(p)
    visited[p] = True    
    for np in graph[p]: 
        if not visited[np]: dfs(np)

bfsret = []
def bfs(p):
    visited[p]= True
    q = [p]
    while q:
        p = q.pop(0)
        bfsret.append(p)
        for np in graph[p]:
            if not visited[np]:
                q.append(np)
                visited[np] = True

def set_data():
    global graph, visited
    n,m,start = map(int,input().split())
    graph = {i+1:list() for i in range(n)}
    visited = [False] * (n+1)
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    for key,value in graph.items():
        graph[key] = sorted(value)
    return start

def reset_visited():
    global visited
    for i in range(len(visited)): visited[i] = False

def run():
    start = set_data()

    reset_visited()
    dfs(start)

    reset_visited()
    bfs(start)

    print(*dfsret)
    print(*bfsret)

run()