def solution(my_string):    
    answer = 0
    cmdq = my_string.split()
    calculation = '+'
    for i in cmdq:
        if i.isdigit():
            if calculation=='+':
                answer+=int(i)
            elif calculation=='-':
                answer-=int(i)
        else:
            calculation=i
    return answer