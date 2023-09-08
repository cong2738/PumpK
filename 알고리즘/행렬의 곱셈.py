# nxn 행렬 곱셈
def mul_matrix(mat1,mat2):
    if len(mat1[0]) != len(mat2): 
        print("rowA != colB")
        return
    
    l,m,n = len(mat1),len(mat1[0]),len(mat2[0])
    res = [[0]*n for _ in range(l)]

    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                # c11 = a11*b11 + a12*b21
                res[i][j] += mat1[i][k] * mat2[k][j]

    return res