import sys
ziped_data = []
readline = sys.stdin.readline
photo = [list(map(int,readline().rstrip())) for _ in range(int(readline()))]
print()
print(*photo,sep='\n')