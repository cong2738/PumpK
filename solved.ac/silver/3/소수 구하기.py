def is_Prime(number):
    if number == 1: return False
    for i in range(2, 1 + int(number**(1/2))):
        if number%i ==0:
            return False
    return True
m,n = map(int,input().split())
for num in range(m,n+1):
    if is_Prime(num):
        print(num)