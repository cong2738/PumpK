def supo(answers, pattern):
    correct = 0
    loop = 0
    for x in answers:
        if(pattern[loop]==x):
            correct+=1
        loop=int((loop+1)%len(pattern))
    return correct

def solution(answers):
    answer = []
    supopattern = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    supoja = [supo(answers, pattern) for pattern in supopattern]      
    m = max(supoja)
    for x in range(0,len(supoja)):
        if supoja[x] == m:
            answer.append(x+1)
    return answer
print(solution([1,3,2,4,2]	))