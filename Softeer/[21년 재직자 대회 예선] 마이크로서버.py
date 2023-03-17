import sys
readline = sys.stdin.readline

def pakaging(itemlist,visited):
    memo = [0]*(N+1)
    for i in range(0,N):
        if visited[i]: continue
        if memo[i]+itemlist[i] > 900:
            return True
        visited[i] = True
        if memo[i] < memo[i]+itemlist[i] <= 900:
            memo[i+1] = memo[i]+itemlist[i]
    return memo[N]

for _ in range(int(readline())):
    N,m = int(readline()), list(map(int,readline().split()))
    cnt = 0
    while(pakaging(m,[False]*N)): cnt += 1
    print(cnt)