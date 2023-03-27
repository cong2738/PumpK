def solution(s):
    answer = 0
    cmd = s.split()
    crz=0
    for i in cmd:
        if(i=='Z'):
            answer-=crz
        else:
            answer+=int(i)
            crz = int(i)
    return answer
print(solution("1 2 3 4 "))