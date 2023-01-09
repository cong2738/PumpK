import sys
memo = {0:1,1:8}
sys.setrecursionlimit(100000)
def rcs(num:int):
    if not num in memo:
        memo[num] = rcs(num-1) + 8
    return memo[num]
N:int = 2**(int(sys.stdin.readline())-1)
rcs(N)
print(sum([memo[num] for num in range(0,N+1)]))
