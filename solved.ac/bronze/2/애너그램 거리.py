import sys
from collections import defaultdict as dd
readline = sys.stdin.readline

def make_dict(word):
        ret = dd(int)
        for c in word:
            ret[c] += 1
        return ret

def comp(a,b):
    ret = 0
    for c in a:
        if a[c] > b[c]:
            ret += a[c] - b[c]
    return ret

def anagram_dist(a,b):
    a,b = make_dict(a),make_dict(b)
    return comp(a,b) + comp(b,a)

N = int(readline())
for i in range(1,N+1):
    A,B = readline().rstrip(),readline().rstrip()
    print(f'Case #{i}: {anagram_dist(A,B)}')