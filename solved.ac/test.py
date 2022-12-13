import sys #입력을 반복해서 마~~~않이 받아야 할때 입력속도를 개선하기위해 사용한다.
getline = sys.stdin.buffer.readline #개행문자빼고 받아오니 주의할것
cout = sys.stdout.write
class pumpK:
    '''*2차원 배열 슬이싱 [(nx,ny):(y,x사이즈)],[(x,y):(자를위치)]'''
    def slice_2D_list(board,x,y,nx,ny):        
        [line[x:x+nx] for line in board[y:y+ny]]
nx,ny = 2,2
Q = [1,2,3,4]
print(Q.pop(-1))
print(Q)