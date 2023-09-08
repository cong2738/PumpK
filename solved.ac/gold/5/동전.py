import sys
from collections import defaultdict as dd
readline = sys.stdin.readline

def knapsck(goal:int,coin_list):
    dp = [0] + [0]*(goal)
    for coin in coin_list:
        dp[coin] = 1

    for value in coin_list:
        for i in range(value,goal+1):
            dp[i] = max(dp[i],dp[i-value])

    return dp[goal]

T = int(readline())
for _ in range(T):    
    _ = int(readline())
    coins = list(map(int,readline().split()))
    target = int(readline())
    print(knapsck(target,coins))