from collections import deque
def solution(numbers):
    res = [-1] * len(numbers)
    stack = deque([])
    for i,n in enumerate(numbers):
        while stack and numbers[stack[-1]] < n:
            res[stack.pop()] = n   
        stack.append(i)  
    return res

print(solution([9, 1, 5, 3, 6, 2]))