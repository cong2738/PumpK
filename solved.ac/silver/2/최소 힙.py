import sys
import heapq
readline = sys.stdin.readline
my_heap = []
for _ in range(int(readline())):
    cmd = int(readline())
    if cmd == 0:
        print(heapq.heappop(my_heap) if my_heap else 0)
    else: heapq.heappush(my_heap,cmd)
