import sys
readline = sys.stdin.readline
N = int(readline())
stair = [0]+[int(readline()) for _ in range(N)]
memo = {1:stair[1],2:max(stair[1]+stair[2],stair[2]),3:max(stair[1]+stair[3],stair[2]+stair[3])}
for i in range(4,N+1):
    memo[i] = max(memo[i-2]+stair[i], memo[i-3]+stair[i-1]+stair[i])

print(memo[N])