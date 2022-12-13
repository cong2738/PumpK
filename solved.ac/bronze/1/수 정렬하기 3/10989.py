import sys
n = int(sys.stdin.readline())
pakage = dict()
for i in range(n):
    in_num = int(sys.stdin.readline())
    if in_num in pakage:
        pakage[in_num] += 1
    else: pakage[in_num] = 1
for key,num in sorted(pakage.items()):
    for i in range(num):
        sys.stdout.write(str(key)+'\n')