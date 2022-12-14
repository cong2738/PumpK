from itertools import combinations
n,m = map(int,input().split())
sum_comb = [sum(cards) for cards in combinations(list(map(int, input().split())),3)]
ret = 0
for cards_sum in sum_comb:
    if cards_sum<=m:
        ret = max(ret,cards_sum)
print(ret)