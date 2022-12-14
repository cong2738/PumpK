import sys
print(*sorted([sys.stdin.readline().strip() for i in range(int(sys.stdin.readline().strip()))], key=lambda x:int(x.split()[0])), sep='\n')