def solution(food):
    answer = ''
    for i in range(1,len(food)):
        answer += str(str(i)*(food[i]//2))
    return answer + '0' + answer[::-1]
print(solution([1,3,4,6]))