from itertools import permutations as pm
import math

def is_prime(x):
    if(x<=1): return 0
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer,pl,pn = 0,list(),set()
    for i in range(1,len(numbers)+1):
        pl+=list(pm(numbers,i))
    for i in pl:
        num = int(''.join(i))
        if is_prime(num):
            pn.add(num)
    return len(pn)
print(solution("011"))
