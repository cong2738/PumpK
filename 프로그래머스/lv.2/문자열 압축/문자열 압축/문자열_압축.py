def solution(s):
    answer = 0
    L = len(s)
    zip = ["" for i in range(L)]
    for i in range(1,L + 1):
        index = 0
        ziped = ''
        while index < L:
            time = 0
            data  = s[index: index+i]
            while(data ==  s[index + i: index + i + i]):
                time+=1
                index += i
            if(time == 0):
                ziped += data
                index += i
            else:
                ziped = ziped + str(time + 1) + data
                index += i
        print(ziped)
        zip[i-1]=len(ziped)
    return min(zip)
print(solution("aaaaaaaaaabbbbbbbbbb "))

