from collections import defaultdict as dd, deque as dq

def bfs(p,graph):
     visited = dd(int)
     visited[p] = 0
     Q = dq([(p,0)])
     while Q:
          p,cnt = Q.popleft()
          for np in graph[p]:
               if not np in visited:
                    Q.append((np,cnt+1))
                    visited[np] = cnt+1
     return visited

def solution(n, roads, sources, destination):
     graph = dd(set)
     for n1,n2 in roads:
          graph[n1].add(n2)
          graph[n2].add(n1)
     root = bfs(destination,graph)
     return [root[p] if p in root else -1 for p in sources]

print(solution(3,[[1, 2], [2, 3]],	[2, 3],1))