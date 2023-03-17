from itertools import permutations

N,M = map(int,input().split())
nums = map(int,input().split())

for x in sorted(set(permutations(nums,M))): print(*x)