import sys
from itertools import combinations_with_replacement
readline = sys.stdin.readline

N,M = map(int,readline().split())
for x in combinations_with_replacement(range(1,N+1),M): print(*x)