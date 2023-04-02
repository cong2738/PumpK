from collections import defaultdict as dd

def make_dict():
    ret = dd(int)
    for c in input():
        ret[c] += 1
    return ret

def comp(a,b):
    ret = 0
    for c in a:
        if a[c] > b[c]:
            ret += a[c] - b[c]
    return ret

a,b = make_dict(),make_dict()

print(comp(a,b) + comp(b,a))