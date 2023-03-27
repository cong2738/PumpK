import sys
from collections import defaultdict as dd
readline = sys.stdin.readline

N,M = map(int,readline().split())
DNA = [dd(int) for _ in range(M)]

for _ in range(N):
    input_DNA = readline().rstrip()
    for i,c in enumerate(input_DNA):
        if c != '.': DNA[i][c] += 1

res = len(max(DNA,key=lambda x:len(x)))
print(res)

'''
4 5
a..tt
gc...
a.g.t
.c.ag
'''