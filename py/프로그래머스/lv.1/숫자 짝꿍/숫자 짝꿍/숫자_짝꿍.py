def solution(X, Y):
    answer = ''
    IX,IY= [X.count(str(i)) for i in range(10)],[Y.count(str(i)) for i in range(10)]    
    for i in range(9,-1,-1):
        answer += str(i)*min(IX[i],IY[i])
    if answer == '':
        return '-1';
    elif answer[0]=='0' and answer[-1]=='0':
        return '0'
    else:
        return answer
print(solution("100","123450"))