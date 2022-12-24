import sys
recursion_max = 100000
memo = [1,1,2,3] + [0]*recursion_max - len(4)
sys.setrecursionlimit(recursion_max)
def tiling(width):
    global memo
    if not memo[width]:
        memo[width] = (tiling(width - 1) + tiling(width - 2))%10007
    return memo[width]

print(tiling(int(input())))