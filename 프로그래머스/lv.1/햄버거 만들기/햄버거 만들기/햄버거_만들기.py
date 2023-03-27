def solution(ingredient):
    answer = 0
    recipe = [1,2,3,1]
    hamburger = []
    for ind in ingredient:
        hamburger.append(ind)
        if hamburger[-4:] == recipe:
            answer += 1
            for i in range(4):
                hamburger.pop()
    return answer
ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
print(solution(ingredient))
