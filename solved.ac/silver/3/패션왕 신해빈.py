import sys
readline = sys.stdin.readline

for _ in range(int(readline())):
    drawer = dict()
    category = list()
    for _ in range(int(readline())):
        clothing,part = readline().split()
        if not part in drawer: 
            category.append(part)
            drawer[part] = 0
        drawer[part] += 1
    res = 1
    for x in drawer.values():
        res *= x+1
    print(res - 1)