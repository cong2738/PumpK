import sys
import heapq
readline = sys.stdin.readline
L=list()
for _ in range(int(readline())):
    cmd = int(readline())
    if cmd: heapq.heappush(L,(-cmd,cmd))
    else: print(heapq.heappop(L)[1] if L else 0)