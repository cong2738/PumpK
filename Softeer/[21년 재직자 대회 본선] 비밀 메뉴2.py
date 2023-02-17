#LCS: Longest Common Subsequence (최장 공통 부분 수열)
import sys
readline = sys.stdin.readline

N,M,K = map(int,readline().split())
A = readline().split()
B = readline().split()
C = [[0]*(M+1) for _ in range((N+1))]
res = 0
for i in range(1,N+1):
    for j in range(1,M+1):
        if A[i-1] != B[j-1]: continue
        C[i][j] = C[i-1][j-1] + 1
        res = max(C[i][j],res)

print(*C,sep='\n')
print(res)