import sys, heapq
readline = sys.stdin.readline
box = []
for _ in range(int(readline())):
    x = int(readline())
    if x == 0: print(heapq.heappop(box)[1] if box else 0)
    else: heapq.heappush(box,(abs(x),x))