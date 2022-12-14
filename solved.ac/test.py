class pumpK:
    import sys #입출력을 반복해서 마~~~않이  할때 입출력속도를 개선하기위해 사용한다.
    readline = sys.stdin.buffer.readline #개행문자까지 받아오니 주의할것
    write = sys.stdout.write #문자열자료형만 받으며 끝에 아무고토 붙혀주지 않아요 니가알아서 만들어 붙히세요
    '''*2차원 배열 슬라이싱 [(nx,ny):(y,x사이즈)],[(x,y):(자를위치)]'''
    def slice_2D_list(board,x,y,nx,ny):        
        [line[x:x+nx] for line in board[y:y+ny]]
from collections import OrderedDict
nx,ny = 2,2
Q = OrderedDict()
Q[2] = 1
Q[1] = 3
print(Q)