import sys
from itertools import combinations as cb
readline = sys.stdin.readline

N = int(readline())
parking_lot = list(map(int,readline().split()))
res = 0
for order in cb(range(1,N+1),3):
    ai,aj,ak = (parking_lot[idx-1] for idx in order)
    if ai < aj and ai > ak: res += 1
print(res)