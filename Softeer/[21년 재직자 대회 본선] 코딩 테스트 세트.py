import sys
readline = sys.stdin.readline

N,T = map(int,readline().split())
for _ in range(T):
    temp = readline().split()
    data = [temp[i:i+2] for i in range(0,len(temp),2)]