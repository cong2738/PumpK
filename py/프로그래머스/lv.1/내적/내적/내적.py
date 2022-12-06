def solution(a, b):
    return sum([A*B for A,B in zip(a,b)])
print(solution([1,2,3,4],[-3,-1,0,2]))
