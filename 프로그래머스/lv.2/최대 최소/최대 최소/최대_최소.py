
def solution(s):
    answer = ''
    L = s.split(' ')
    M=int(L[0])
    m=int(L[0])
    for i in L:
        print(i)
        M=max(int(i),M)
        m=min(int(i),m)
    return str(m)+' '+str(M)
print(solution("-1 -2 -3 -4"))