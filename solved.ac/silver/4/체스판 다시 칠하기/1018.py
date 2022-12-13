import math
board = list()
pattern = ["WB","BW"]
n,m = map(int,input().split())
for i in range(n):
    board.append(list(input()))
numofpaint = math.inf
for y in range(n-7):
    for x in range(m-7):
        chessboard = [line[x:x+8] for line in board[y:y+8]]
        count0,count1 = 0,0
        for i in range(8):
            for j in range(8):
                if chessboard[i][j] != pattern[i%2][j%2]: count0 += 1
                if chessboard[i][j] != pattern[(i+1)%2][j%2]: count1 += 1
        numofpaint = min(numofpaint,count0,count1)
print(numofpaint)
