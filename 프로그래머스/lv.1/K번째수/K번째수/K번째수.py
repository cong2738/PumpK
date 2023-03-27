def solution(array, commands):    
    return [(lambda x: sorted(array[x[0]-1:x[1]])[i[2]-1])(i) for i in commands]
ar = [1, 5, 2, 6, 3, 7, 4]	
cmd = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	
print(solution(ar,cmd))

