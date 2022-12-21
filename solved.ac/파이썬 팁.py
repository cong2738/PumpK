#sort returns "List"
class pumpK:
    import sys 
    readline = sys.stdin.buffer.readline 
    write = sys.stdout.write 
    sys.setrecursionlimit(1000000) 
   
    '''*slice 2D list'''
    def slice_2D_list(board,x,y,dx,dy):        
        [line[x:x+dx] for line in board[y:y+dy]]

    import heapq # Min_heap
    L = list()
    num,index = 1,0
    heapq.heapify(L)
    heapq.heappush(L,num) 
    heapq.heappop(L)    
    heapq.heappush(L,(-num,num)) #max_hip by using heapq
from collections import deque 
List = [1,111,11,1111,22222,6,4,21]
print(List)
import heapq
heapq.heapify(List)
print(List)
