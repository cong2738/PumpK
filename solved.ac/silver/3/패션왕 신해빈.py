from itertools import combinations as cb
import sys
readline = sys.stdin.readline

def mult_all(L:iter):
    ret = 1
    for x in L:
        ret *= x
    return ret

for _ in range(int(readline())):
    drawer = dict()
    category = list()
    for _ in range(int(readline())):
        clothing,part = readline().split()
        if not part in drawer: 
            category.append(part)
            drawer[part] = 0
        drawer[part] += 1