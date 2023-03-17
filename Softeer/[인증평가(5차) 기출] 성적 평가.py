import sys
from collections import defaultdict
readline = sys.stdin.readline

N = int(readline())
people = [0]*N
standings = [defaultdict(list) for _ in range(4)]
ranks = [[0]*N for _ in range(4)]

#3개의 경기
for i in range(3):
    contest = list(map(int, readline().split())) #입력받음
    #인간들이 어떤 점수에있는지 저장
    for n,score in enumerate(contest):
        standings[i][score].append(n)
        people[n] += score    

#인간들이 어떤 점수(총점)에있는지 저장
for n,score in enumerate(people):
    standings[3][score].append(n)

#점수를 내림차순으로 정렬후 각 점수의 인간의 등수판별
for i,D in enumerate(standings):
    L = sorted(D.items(),key=lambda x:x[0],reverse=True)
    R = 0
    for score,people in L:        
        for p in people:
            ranks[i][p] = 1 + R
        R += len(people)

#각 경기 및 총점에 대한 등수 출력 
for rank in ranks: print(*rank)