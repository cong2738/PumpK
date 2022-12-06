def solution(lines):
    answer = 0
    line = []
    for x in range(-100,101):
        line.append(0)
    for x in lines:        
        for i in range(int(x[0]),int(x[1])):
            line[i]+=1
    return len(line)-line.count(1)-line.count(0)
print(solution(	[[0, 1], [2, 5], [3, 9]]))