from functools import reduce
from itertools import combinations

yeondu = input()
case_num = int(input())
case = sorted([input() for i in range(case_num)])
count_letter = lambda name,letter : name.count(letter)
yeondu_LOVE = [count_letter(yeondu,L) for L in 'LOVE']
LOVE = [reduce(lambda x,y : x * y,[sum(tp) for tp in list(combinations([(count_letter(tc,'LOVE'[i]) + yeondu_LOVE[i]) for i in range(4)],2))])%100 for tc in case]    
print(case[LOVE.index(max(LOVE))])