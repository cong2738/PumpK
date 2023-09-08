from math import lcm
from itertools import combinations

n = map(int,input().split())

combs = [lcm(*comb) for comb in combinations(n,3)]

print(min(combs))