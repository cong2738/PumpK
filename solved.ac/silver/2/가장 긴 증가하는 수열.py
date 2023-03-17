import sys
readline = sys.stdin.readline

N = int(readline())
A = list(map(int,readline().split()))

memo = [[0,1] for _ in range(N)]
memo[0] = [A[0],1]

for i in range(1,N):
    num,cnt = 0,0
    for j in range(0,i):
        if memo[j][0] >= A[i] or cnt >= memo[j][1]: continue        
        num,cnt = memo[j]
    memo[i] = [A[i],cnt+1]

print(max(memo,key=lambda x:x[1])[1])