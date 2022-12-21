import sys
readline = sys.stdin.readline
data = [list(map(int, readline().split())) for _ in range(int(readline()))]
data.sort(key=lambda x:(x[1],x[0]))

#greedy
time, cnt = 0, 0
for start,end in data:
    if  time <= start:
        time = end
        cnt += 1
print(cnt)
