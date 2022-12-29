from itertools import permutations as pm
N,M = map(int,input().split())
numlist = list(map(int,input().split()))

for c in sorted(pm(numlist,M)):
    print(*c)