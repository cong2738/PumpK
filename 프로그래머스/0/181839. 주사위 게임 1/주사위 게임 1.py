def solution(a, b):
    ai, bi = a%2, b%2
    if(ai and bi): return a**2 + b**2
    elif(ai or bi): return 2*(a+b)
    return abs(a-b)