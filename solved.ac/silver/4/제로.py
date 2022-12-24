from collections import deque
import sys
input = sys.stdin.readline
box = deque()
for _ in range(int(input())):
    cmd = int(input())
    if cmd: box.append(cmd)
    else: del box[-1]
print(sum(box))