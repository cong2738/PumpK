def solution(myString:str, pat):
    answer = 0
    idx = 0
    while idx < len(myString):
        myString = myString[idx:]
        find = myString.find(pat)
        if find == -1: break
        answer += 1
        idx = find + 1
    return answer