
tc = int(input())
for t in range(tc):
    input()
    n,m=map(int,input().split());
    jun = list(map(int,input().split()))
    bee = list(map(int,input().split()))
    mj,mb = max(jun), max(bee)
    if mj < mb: print('B')
    else: print('S')
