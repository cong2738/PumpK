import sys
sys.setrecursionlimit(100000)
def fpow(C,n):
    if n == 1:
        return C
    x = fpow(C,n//2)
    if n %2 == 0: return x*x
    return x*x*C

def nacci(n):
    global fibo
    if n in fibo: return fibo[n]
    fibo[n] = (nacci(n-1) + nacci(n-2))%1_000_000_007
    return fibo[n]  

N = int(input())
fibo = {0:0,1:1}
nacci(N)
print(fibo[N])