def add(num):
    ret = 0
    for i in range(num):
        ret += i
    return ret
def solution(num, total):
    ret = []
    a = int((total-add(num))/num)
    for i in range(num):
        ret.append(a+i)
    return ret
