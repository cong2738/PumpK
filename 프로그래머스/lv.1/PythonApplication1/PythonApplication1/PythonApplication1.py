from itertools import combinations as comb
def solution(numbers):
    return sorted(list({a+b for a,b in comb(numbers,2)}))
numbers = [0,1,3,4,1]
print(solution(numbers))
