import sys
readline = sys.stdin.readline

N,M = map(int,readline().split())
board = [list(map(int,readline().split()))for _ in range(N)]

prefix = [[0]*(N+1) for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        prefix[i+1][j+1] = prefix[i][j+1] + prefix[i+1][j] - prefix[i][j] + board[i][j]

for _ in range(M):
    x1,y1,x2,y2 = map(int,readline().split())
    s = prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1]
    print(s)