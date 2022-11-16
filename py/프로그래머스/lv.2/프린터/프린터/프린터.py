
def solution(priorities, location):
    p = []
    for i in range(0,len(priorities)):
        p.append([priorities[i],i+1])
    p.sort(reverse=True)
    print(p)
    answer = p[location][1]
    return answer
p=[2, 1, 3, 2]	
l=2
print(solution(p,l))