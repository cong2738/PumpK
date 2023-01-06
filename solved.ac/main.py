import sys
readline = sys.stdin.readline
for i in range(1,int(readline())+1):
    print(f'Case #{i}: {sum(map(int,readline().split()))}')