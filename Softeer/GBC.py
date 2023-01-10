import sys
readline = sys.stdin.readline
N,M = map(int,readline().split())
section = [0]*101
start = 1
for i in range(N):
    dh,limit = map(int,readline().split())
    for j in range(start,start+dh):
        section[j] = limit
    start += dh
res = [0]*M
start = 1
for i in range(M):
    dh,speed = map(int,readline().split())
    for j in range(start,start + dh):
        res[i] = max(res[i],speed-section[j])
    start += dh
print(max(res))