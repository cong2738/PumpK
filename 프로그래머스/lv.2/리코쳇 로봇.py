from collections import deque

def find_robo(board):
    for y,line in enumerate(board):
        for x,c in enumerate(line):
            if c == 'R': return x,y

def solution(board):
    move = ((1,0),(-1,0),(0,1),(0,-1))
    LX,LY = len(board[0]), len(board)    
    robo = find_robo(board)

    visited = [[0]*(LX) for _ in range(LY)]
    visited[robo[1]][robo[0]] = 1

    Q = deque([robo])
    while Q:
        x,y = Q.popleft()
        if board[y][x] == 'G': return visited[y][x] - 1

        for dx,dy in move:
            nx,ny = x,y
            while 0 <= nx + dx < LX and 0 <= ny + dy < LY and board[ny+dy][nx+dx] != 'D':
                nx += dx
                ny += dy

            if not visited[ny][nx]:
                visited[ny][nx] = visited[y][x] + 1
                Q. append((nx,ny))

    return -1


################################################################
print(solution(
        [
            "...D..R", 
            ".D.G...", 
            "....D.D", 
            "D....D.", 
            "..D...."
        ]
    )
)