def solution(n):
    answer = 0
    for x in range(0,n):                
        answer+=1     
        while(answer != 0 and (answer%3)==0) or (str(answer).find('3')!=-1):
            print("*")
            answer+=1
        print(answer)
    return answer
print(solution(15))