def solution(a, b):
    answer = 0
    cal1 = int(str(a)+str(b))
    cal2 = 2*a*b
    answer = cal1 if cal1>cal2 else cal2
    return answer