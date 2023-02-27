import sys
from itertools import permutations as pm
def work(rail):
    res = 0
    target = 0
    weight = 0
    for _ in range(K):
        while weight+rail[target] <= M:
            weight += rail[target]
            target += 1
            target %= N
        res += weight
        weight = 0
    return res
readline = sys.stdin.readline
N,M,K = map(int,readline().split())
line = map(int,readline().split())
res = min([work(sample) for sample in pm(line,N)])
print(res)