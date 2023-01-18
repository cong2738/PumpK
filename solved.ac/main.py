from itertools import combinations as cb
L = [1,2,3]
for i in range(len(L)+2):
    print(*cb(L,i))