import sys
readline = sys.stdin.readline
time = list()
for _ in range(int(readline())):
    time.append(list(map(int, readline().split())))
time.sort(key=lambda x:(x[1]-x[0],x[0]))
print(*time,sep='\n')
