import sys
readline = sys.stdin.readline
LED = [0b1111110,0b1100000,0b1011011,0b1110011,0b1100101,0b0110111,0b0111111,0b1100110,0b1111111,0b1110111]
def eeeee(l:list):
    while(len(l) < 5):
        l = [0]+l
    return l
res = [0]*5
for _ in range(int(readline())):
    start,end = map(eeeee,map(lambda s:[LED[int(c)] for c in s],readline().split()))
    for i,(s,e) in enumerate(zip(start,end)): res[i] = s^e
    cnt = 0
    for b in res: cnt += bin(b)[2:].count('1')
    print(cnt)