import sys
from collections import defaultdict as dd
readline = sys.stdin.readline

def set_schedule(time):
    cnt = 0
    while time in schedule:
        time = schedule[time]
        cnt += 1
    return cnt

schedule = [0]*10
N = int(readline())
for _ in range(N):
    s,e = map(int,readline().split())
    for i in range(s,e):
        schedule[i]+=1

print(schedule)