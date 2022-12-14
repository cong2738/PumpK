import sys
n = int(sys.stdin.readline())
pakage = [0 for i in range(10010)]
for i in range(n):
    in_num = int(sys.stdin.readline())
    pakage[in_num] += 1
for index in range(len(pakage)):
    for i in range(pakage[index]):
        sys.stdout.write(str(index)+'\n')