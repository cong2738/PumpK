import sys
memo = {1:0,2:0,3:1,4:0,5:1,6:2,7:0}
sys.setrecursionlimit(1000000)
def baedal(n):
    global memo
    if not n in memo:
        b5 = baedal(n-5)
        b3 = baedal(n-3)
        if b5:memo[n] = b5 + 1
        elif b3: memo[n] = b3 + 1
        else: memo[n] = 0
    return memo[n]
ret = baedal(int(input()))
print(ret if ret else -1)