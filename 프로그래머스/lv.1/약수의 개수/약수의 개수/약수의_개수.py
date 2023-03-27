def solution(left, right):
    dec = lambda x : -1 if (x**0.5).is_integer() else 1
    return sum([i*dec(i) for i in range(left,right+1)])
print(solution(1,4))
