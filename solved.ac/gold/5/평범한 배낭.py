import sys
readline = sys.stdin.readline
N,K = map(int,readline().split())
itemlist = [0]+[list(map(int,readline().split())) for i in range(N)] #[[W,V],~~]
memo = [[0]*(K+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,K+1):
        if j - itemlist[i][0] >= 0: 
            memo[i][j] = max(memo[i-1][j],memo[i-1][j-itemlist[i][0]]+itemlist[i][1])
        else: 
            memo[i][j] = memo[i-1][j]
print(memo[N][K])
