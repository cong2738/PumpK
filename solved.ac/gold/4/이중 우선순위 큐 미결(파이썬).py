import sys
import heapq
input = sys.stdin.readline
for _ in range(int(input())):
    L = []
    heapq.heapify(L)
    for _ in range(int(input())):
        cmd = input().rstrip().split()
        if cmd[0] == 'I':
            heapq.heappush(L,int(cmd[1]))
        elif cmd[0] == 'D' and L:            
            if cmd[1] == '-1': heapq.heappop(L)
            else: L.pop()
    print((max(L), min(L)) if L else "EMPTY")