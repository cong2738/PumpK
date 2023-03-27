def solution(a, b, n):
    answer = 0
    while(n>=a):
        nb = b * (n//a);
        n = n%a + nb
        answer+=nb
    return answer
print(solution(3,2,20))
