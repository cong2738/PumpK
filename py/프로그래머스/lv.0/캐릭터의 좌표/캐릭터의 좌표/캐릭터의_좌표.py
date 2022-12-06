def solution(keyinput, board):
    answer = [0,0]
    move = {'up':[0,1],'down':[0,-1],'right':[1,0],'left':[-1,0]}
    for x in keyinput:
        nx = move[x][0] + answer[0]
        ny = move[x][1] + answer[1]        
        if((-board[0]/2 <= nx <= board[0]/2) and (-board[1]/2 <= ny <= board[1]/2)):
            answer = [nx,ny]
            
    return answer
print(solution(	["down", "down", "down", "down", "down"], [7, 9]))
