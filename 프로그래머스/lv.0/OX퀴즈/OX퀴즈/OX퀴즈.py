def solution(quiz):
    answer = []
    for i in quiz:
        LR = i.split('=')
        tmp = LR[0].split()
        if tmp[1] == '+':
            LR[0] = int(tmp[0])+int(tmp[2])
        if tmp[1] == '-':
            LR[0] = int(tmp[0])-int(tmp[2])
        LR[1] = int(LR[1])
        if LR[0]==LR[1]:
                answer.append('O')
        else:
            answer.append('X')
    return answer
print(solution(["3 - 4 = -3", "5 + 6 = 11"]))