import sys
input = sys.stdin.readline
print(*sorted([input().strip() for i in range(int(input()))], key=lambda x:list(map(int, x.split()))),sep='\n')