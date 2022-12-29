import sys
from math import inf
readline = sys.stdin.readline
N,K = map(int,readline().split())
itemlist = [list(map(int,readline().split()))+[i] for i in range(N)]
print(itemlist)
