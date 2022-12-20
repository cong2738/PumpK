#sort returns "List"
class pumpK:
    import sys 
    readline = sys.stdin.buffer.readline 
    write = sys.stdout.write 
    sys.setrecursionlimit(1000000) 
   
    '''*2???? ??? ???????'''
    def slice_2D_list(board,x,y,nx,ny):        
        [line[x:x+nx] for line in board[y:y+ny]]

    import heapq # Min_heap
    L = list()
    num,index = 1,0
    heapq.heapify(L)
    heapq.heappush(L,num) 
    heapq.heappop(L)    
    heapq.heappush(L,(-num,num)) #heapq를 사용하여 max_heap을 쓰는 트릭

from collections import deque 
List = [1,111,11,1111,22222,6,4,21]
print(List)
import heapq
heapq.heapify(List)
print(List)
