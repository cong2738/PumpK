def fac(num):
    ret = 1
    for x in range(1,num + 1):
        ret *= x
    return ret
def solution(balls, share):
    return fac(balls)/(fac(balls-share)*fac(share))