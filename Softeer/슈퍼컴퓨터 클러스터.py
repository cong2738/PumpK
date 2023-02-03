#2진탐색 사용
import sys
from collections import defaultdict as dd
readline = sys.stdin.readline
(N,B),a = map(int,readline().split()),dd(int)
for n in map(int,readline().split()): a[n] += 1
min = 0
max = sys.maxsize
k = a.keys()
while(min <= max):
    cost = 0
    mid = int((max+min)/2)
    possible = True
    for n in k:
        if mid <= n: continue
        temp = mid - n
        cost += a[n] * temp**2
        if B < cost:
            possible = False
            break
    if possible: min = mid+1
    else: max = mid-1
print(mid,max)