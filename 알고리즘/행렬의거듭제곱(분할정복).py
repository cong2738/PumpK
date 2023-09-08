# nxn 행렬 곱셈
def mult_mat(mat1,mat2):
    if len(mat1[0]) != len(mat2): 
        print("rowA != colB")
        return
    
    l,m,n = len(mat1),len(mat1[0]),len(mat2[0])
    res = [[0]*n for _ in range(l)]

    for i in range(l):
        for j in range(m):
            for k in range(n):
                # c11 = a11*b11 + a12*b21
                res[i][j] += mat1[i][k] * mat2[k][j]

    return res

# 행렬의 거듭제곱 (분할정복 사용)
def pow_mat(mat,n):
    if n == 1:
        return mat    
    
    tmp = pow_mat(mat,n//2)

    if n%2 == 0: return mult_mat(tmp,tmp)  
      
    return mult_mat(mult_mat(tmp,tmp),mat)

