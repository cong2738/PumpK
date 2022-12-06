def solution(n):
    answer = set()
    pr = 2
    while n>1:
        if int(n%pr)==0:
            n = int(n/pr)
            answer.add(pr)
        else:
            pr+=1    
    return sorted(list(answer))
print(solution(12))
