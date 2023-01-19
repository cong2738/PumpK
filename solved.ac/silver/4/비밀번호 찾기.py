import sys
readline = sys.stdin.readline
N,M = map(int,readline().split())
site = dict()
for _ in range(N):
    st,ps = readline().split()
    site[st] = ps
print('\n'.join([site[readline().rstrip()] for _ in range(M)]))