from collections import deque
#visited정보 저장을 dictionaly에 함
'''
def bfs(n, end):
    visited = {n:0}
    if n == end: return 0
    q = deque([n])
    while q:
        n = q.popleft()
        if n == end: return visited[n]
        move = [n-1,n+1,2*n]
        for np in move:
            if not np in visited and 0 <= np <= 100000:
                visited[np] = visited[n] + 1
                q.append(np)
n,k = map(int,input().split())
print(bfs(n,k))
'''
#visited정보저장을 list에 함
from collections import deque
def bfs(n, end):
    visited = [False for _ in range(100001)]
    if n == end: return 0
    q = deque([n])
    while q:
        n = q.popleft()
        if n == end: return visited[n]
        move = [n-1,n+1,2*n]
        for np in move:
            if 0 <= np <= 100000 and not visited[np]:
                visited[np] = visited[n] + 1
                q.append(np)
n,k = map(int,input().split())
print(bfs(n,k))