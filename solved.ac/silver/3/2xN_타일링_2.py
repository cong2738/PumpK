import sys
readline = sys.stdin.readline
memo = {1:1,2:3}

sys.setrecursionlimit(100000)
def dp(n:int):
    if not n in memo:
        memo[n] = dp(n-1) + 2*dp(n-2)
    return memo[n] % 10007
print(dp(int(readline())))