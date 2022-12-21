import sys
readline = sys.stdin.readline
num_of_com = int(readline())
visited = [False for _ in range(num_of_com + 1)]
graph = dict()
for _ in range(int(readline())):
    a,b = map(int,readline().split())
    if a in graph: graph[a].add(b)
    else: graph[a] = {b}
    if b in graph: graph[b].add(a)
    else: graph[b] = {a}
#dfs
sys.setrecursionlimit(1000000)
def spred(parent):
    global visited, graph
    children = graph[parent]
    visited[parent] = True
    for child in children:
        if not visited[child]: spred(child)
spred(1)
print(visited.count(True) - 1)