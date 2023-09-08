import sys
readline = sys.stdin.readline

# 입력
def input():
    N,B = map(int,readline().split())
    mat = [list(map(int,readline().split())) for _ in range(N)]
    return mat,B

# n x n 행렬 곱셈
def mult_mat(mat1,mat2):
    n = len(mat1)
    res = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += mat1[i][k] * mat2[k][j]
            res [i][j] %= 1000
                
    return res

# 행렬 거듭제곱
def pow_mat(mat,n):
    if n == 1:
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] %= 1000
        return mat
    
    tmp = pow_mat(mat,n//2)
    if n%2 == 0:
        return mult_mat(tmp,tmp)
    
    return mult_mat(mult_mat(tmp,tmp),mat)

# main
for row in pow_mat(*input()):
    print(' '.join(map(str,row)))