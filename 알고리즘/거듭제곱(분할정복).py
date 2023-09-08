def fpow(C,n):
    if n == 1:
        return C
    tmp = fpow(C,n//2)
    if n %2 == 0: return tmp*tmp
    return tmp*tmp*C