import sys
readline = sys.stdin.readline
sys.setrecursionlimit(100000)

memo = {1:1,2:1,3:1}
def rcs(n):
    if not n in memo: 
        memo[n] = rcs(n-2) + rcs(n-3)
    return memo[n]

for _ in range(int(readline())): 
    print(rcs(int(readline())))