import sys
from collections import deque as dq, defaultdict as dd
readline = sys.stdin.readline

def move():
    move_list = []
    for i in range(4):
        if not cross_roads[i] or cross_roads[i-1]: continue
        move_list += [i]
    for i in move_list:
        cross_roads[i] -= 1
        print(time+1)

def flag():
    for road in cross_roads:
        if road: return True
    return False

N = int(readline())
cross_roads = [0]*4
time_stamp = dd(list)
for _ in range(N):
    t,w = readline().split()
    time_stamp[int(t)-1].append(ord(w)-ord('A'))

for time in time_stamp:
    for way in time_stamp[time]:
        cross_roads[way] += 1
    move()

while(flag()): 
    time += 1
    move()    