def solution(polynomial):
    answer = ''    
    cmd = polynomial.replace('+','').split()
    eq = {'x':0,'0':0}
    for i in cmd:
        if i[-1] == 'x':
            if i[0:-1] == '':
                num = 1
            else:
                num = int(i[0:-1])
            eq['x'] += num
        else:
            eq['0'] += int(i)
    tmp = []
    for k,v in eq.items():
        if v!=0:
            if k!='0':
                if v==1:
                    tmp.append(k)
                else:
                    tmp.append(str(v)+k)
            else:
                tmp.append(str(v))
    if(len(tmp)==2):
        answer = tmp[0] + ' + ' + tmp[1]
    else:
        answer = tmp[0]
    return answer
print(solution("3x + 7 + x"	))
