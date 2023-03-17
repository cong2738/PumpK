import sys
from itertools import combinations_with_replacement
readline = sys.stdin.readline

N,M = map(int,readline().split())
nums = sorted(map(int,readline().split()))
for x in combinations_with_replacement(nums,M): print(*x)