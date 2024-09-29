import sys

readline = sys.stdin.readline

N = int(readline())
t = list(map(int, readline().split()))
t.sort()

sl = []
max_sl = 0
if N%2 == 1:
    sl.append(t.pop())
    

l = len(t)
for i in range(int(l/2)):
    sl.append(t[i] + t.pop())

print(max(sl))