def solution(score):
    answer = []
    for i in score:
        answer.append((i[0]+i[1])/2)
    rank = sorted(answer,reverse=True)
    for i in range(len(answer)):
        answer[i] = rank.index(answer[i])+1
    return answer
print(solution([[80, 70], [90, 50], [40, 70], [50, 80]]))
