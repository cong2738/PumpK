def solution(sides):      
    return min(sides) + sides[0] + sides[1] - max(sides) - 1
print(solution([3,6]))