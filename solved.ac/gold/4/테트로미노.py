import sys
readline = sys.stdin.readline
move = [(-1,0),(1,0),(0,1),(0,-1)]
result = 0

def dfs(x:int,y:int,sum_value:int,depth:int):
    global result
    if depth >= 4:
        result = max(result,sum_value)
        return
    for dx,dy in move:
        nx,ny = x+dx,y+dy
        if not (0 <= nx < M and 0 <= ny < N and not visited[ny][nx]): continue
        visited[ny][nx] = True
        dfs(nx,ny,sum_value+board[ny][nx],depth+1)
        visited[ny][nx] = False
def check_exshape(x:int,y:int):
    nums = [0]*4
    zero_cnt = 0
    for i,(dx,dy) in enumerate(move):
        nx,ny = x+dx,y+dy
        if not (0 <= nx < M and 0 <= ny < N): 
            zero_cnt += 1
            continue
        nums[i] = board[ny][nx]
    if zero_cnt >= 2: return 0
    ret = board[y][x] + sum(nums)
    return ret if zero_cnt else ret - min(nums)

N,M = map(int,readline().split())
board = [list(map(int,readline().split())) for _ in range(N)]
score = [[0]*N for _ in range(M)]
visited = [[False]*M for _ in range(N)]
for y in range(N):
    for x in range(M):
        visited[y][x] = True
        dfs(x,y,board[y][x],1)
        visited[y][x] = False
        result = max(result,check_exshape(x,y))
print(result)