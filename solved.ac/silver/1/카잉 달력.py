import sys,math
readline = sys.stdin.readline
lcm = math.lcm

for _ in range(int(readline())):
    M,N,x,y = map(int,readline().split())
    maxYear = lcm(M,N)
    while True:
        if x > maxYear or (x-1)%N +1 == y: break
        x += M
    print(-1 if x > maxYear else x)