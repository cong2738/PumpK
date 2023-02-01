import sys
readline = sys.stdin.readline

N,M = map(int,readline().split())

# 0부터 i까지의 합을 계산하여 리스트로 저장(누적합저장)
S = [0] + list(map(int,readline().split()))
for i in range(1,len(S)): S[i] += S[i-1]

# e까지의 합에서 (s-1)까지의 합을 빼면 s부터 e까지의 합이 나온다
for _ in range(M): 
    s,e = map(int,readline().split())
    print(S[e]-S[s-1])

#O(N+M)