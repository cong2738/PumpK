def solution(board):
    for n in range(min(len(board),len(board[0])),1,-1):
        lt1,lt2 = len(board) - n + 1,len(board[0]) - n + 1
        for y in range(lt1):
            sq =board[y :y + n]
            count =0
            for x in range(lt2):
                line = list()
                for i in sq:
                    line += i[x:x+n]
                if not 0 in line: return n*n
    for i in board:
        if(0 in i): return 1
    return 0
board = [[0, 0, 1, 1], [1, 1, 1, 1]]
print(solution(board))
