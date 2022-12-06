def solution(A, B):
    ret = 0
    l = len(A)
    if A==B:
        return 0    
    for j in range(l):
        c = A[-1]
        A = c+A[0:l-1]
        ret+=1
        if A==B:
            return ret
    return -1
print(solution('hello','ohell'))
