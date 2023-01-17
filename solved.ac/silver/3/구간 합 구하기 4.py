import sys
readline = sys.stdin.readline

N,M = map(int,readline().split())
S = [0] + list(map(int,readline().split()))
for i in range(1,len(S)): S[i] += S[i-1]
for _ in range(M): 
    s,e = map(int,readline().split())
    print(S[e]-S[s-1])