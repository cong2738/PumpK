def solution(n):
    answer = [[int(i==j) for j in range(n)] for i in range(n)]
    return answer