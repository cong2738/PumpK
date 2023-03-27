def solution(sizes):    
    sizes = [[min(i),max(i)] for i in sizes] 
    return (lambda x,y:x*y)(max(sizes,key = lambda x:x[0])[0],max(sizes,key = lambda x:x[1])[1])
a=[[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
print(solution(a))
