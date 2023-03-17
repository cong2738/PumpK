from itertools import product
 
def is_not_orderded(L):
    temp = 0
    for n in L:
        if temp > n: return False
        temp = n
    return True

N,M = map(int,input().split())
nums = map(int,input().split())
for x in filter(is_not_orderded,sorted(set(product(nums,repeat=M)))): print(*x)
