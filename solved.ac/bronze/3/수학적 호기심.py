import sys
readline = sys.stdin.readline

for _ in range(int(readline())):
    n,m = map(int,readline().split())
    cnt = 0
    for a in range(1,n):
        for b in range(1+a,n):
            cnt += (((a*a+b*b+m)%(a*b)) == 0)
    print(cnt)