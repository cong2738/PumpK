from itertools import combinations as comb
def solution(X, Y):
    answer = ''
    inter = list(X) & list(Y)    
    if not inter:
        return '-1'    
    return ''.join(sorted(inter,reverse=True))
print(solution('5525','1255'))
