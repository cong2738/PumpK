import math
def is_prime_num(n):
    if(n==1): return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
def solution(n):
    answer = 0
    for i in range(2,n+1):
        if is_prime_num(i):
            answer+=1
    return answer