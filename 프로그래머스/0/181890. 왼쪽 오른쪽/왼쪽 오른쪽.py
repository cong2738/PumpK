def solution(str_list):
    answer = []
    flag = 0
    for i,c in enumerate(str_list):
        if c == 'l':
            answer = str_list[:i]
            break
        if c == 'r':
            answer = str_list[i+1:]
            break
    return answer