#이진탐색(단순 정렬된 리스트상 이진탐색)

import sys
readline = sys.stdin.readline

def treesum(cut_hight):
    sum = 0
    for i in range(N):
        sum += trees[i] - cut_hight if trees[i] > cut_hight else 0
    return sum

N,M = map(int, readline().split())
trees = list(map(int,readline().split()))
trees.sort()

res = 0
low, high = 0, trees[N-1]

while low <= high:
    cut = round((low + high)/2)
    if treesum(cut) >= M:
        low = cut + 1
    else: 
        high = cut -1

print(high)