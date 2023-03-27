from collections import deque

def bfs(s):
    move = [0,lambda x:x-1,lambda x:int(x/2), lambda x:int(x/3)]

    Q,visited = deque([s]),{s:[s]}
    while Q:
        p = Q.popleft()
        
        if p == 1: return visited[1]

        for i in range(1,3+1):
            if p%i: continue
            np = move[i](p)
            if np in visited: continue
            visited[np] = visited[p]+[np]
            Q.append(np)
    
    return -1

res = bfs(int(input()))
print(len(res)-1)
print(*res)