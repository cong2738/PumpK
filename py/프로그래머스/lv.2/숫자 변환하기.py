from collections import deque

def solution(s, t, n):
    move = [lambda a:a+n,lambda a:a*2, lambda a:a*3]
    visited = {s:0}
    q = deque([s])
    while q:
        p = q.pop()
        for mv in move:
            np = mv(p)
            if np > t: continue
            visited[np] = min(visited[np],visited[p]+1) if np in visited else visited[p]+1
            q.append(np)
    return visited[t] if t in visited else -1
xxx = solution(2,1000000,4)
print(xxx)