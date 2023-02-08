#누적 합
import sys
readline = sys.stdin.readline
N,K = map(int,readline().split())
prefix_sum = [0] + list(map(int,readline().split()))
for i in range(1,N+1): prefix_sum[i] += prefix_sum[i-1]
for _ in range(K):
    A,B = map(int,readline().split())
    s = prefix_sum[B]-prefix_sum[A-1]
    n = B-A+1
    print(f'{s/n:.2f}')