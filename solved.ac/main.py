from collections import deque
def bfs(start,end,board):
    visited = [[0]*len(map[0]) for _ in range(len(map))]
    visited[start[1]][start[0]] = True
    move = ()
    Q = deque([start])    
    while Q:
        x,y = Q.popleft()
        if (x,y) == end: return visited
        for dx,dy in move:
            nx,ny = x+dx,y+dy
            if 0 <= nx < len(map[0]) and 0 <= ny < len(map) and not visited[ny][nx] and not board[ny][nx]:
                Q.append((nx,ny))
                visited[ny][nx] = 1
    return []
