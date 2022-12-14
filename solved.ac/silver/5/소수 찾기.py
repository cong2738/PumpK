def is_Prime(number):
    if number == 1: return False
    for i in range(2, 1 + int(number**(1/2))):
        if number%i ==0:
            return False
    return True
input(), print([is_Prime(num) for num in list(map(int,input().split()))].count(True))