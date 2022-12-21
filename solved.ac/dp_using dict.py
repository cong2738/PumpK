memo = {0:1,1:1,2:2,3:3}
def tiling(width):
    global memo
    if not width in memo:
        memo[width] = (tiling(width - 1) + tiling(width - 2))%10007
    return memo[width]

print(tiling(int(input())))