import sys
readline = sys.stdin.readline
N,K = map(int,readline().split())
scores = list(map(int,readline().split()))
for _ in range(K):
    A,B = map(int,readline().split())
    l = scores[A-1:B]
    print(f'{round(sum(l)/len(l),2):.2f}')