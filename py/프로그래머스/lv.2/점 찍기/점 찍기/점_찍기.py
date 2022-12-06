def solution(k, d):
    answer = 0
    dd = d*d
    for i in range(d*d+1):
        for j in range(d*d+1):
            if k*k * i*i + k*k * j*j <= dd:
                answer+=1
    return answer