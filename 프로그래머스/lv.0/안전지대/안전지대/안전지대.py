def solution(board):
    answer = 0
    np = [[0,0],[0,1],[0,-1],
          [1,0],[1,1],[1,-1],
          [-1,0],[-1,1],[-1,-1]]    
    n,m = len(board),len(board[0])
    DA = [[0 for i in range(n)] for j in range(m)]
    for i in range(n):        
        for j in range(m):
            if board[i][j]==1:
                for p in np:                    
                    ni=i+p[0]
                    nj=j+p[1]
                    if 0<=ni<n and 0<=nj<m:
                        DA[ni][nj]=1
    for l in DA:
        answer+=l.count(0)
    return answer

