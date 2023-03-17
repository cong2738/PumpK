import sys
readline = sys.stdin.readline

A, B = readline().rstrip(), readline().rstrip()
Al,Bl = len(A),len(B)
#memorize
LCS = [[str() for _ in range(len(B)+1)] for _ in range(len(A)+1)]
for i in range(Al):
    for j in range(Bl):
        if A[i] == B[j]: LCS[i+1][j+1] = LCS[i][j] + A[i]
        else: LCS[i+1][j+1] = max(LCS[i][j+1], LCS[i+1][j], key=lambda x:len(x))
res1 = len(LCS[-1][-1])
res2 = LCS[-1][-1]
print(res1, res2, sep='\n')