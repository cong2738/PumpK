def solution(n):
    three, index = '', 0
    while(n!=0):        
        three = str(n%3)+three
        n//=3
    return int(three,3)
print(solution(45))
