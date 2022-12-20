memo = {0:[1,0],1:[0,1],2:[1,1]}
def fibonacci(n):
    if not n in memo:
        memo [n] = list(map(sum,zip(fibonacci(n-1), fibonacci(n-2))))
    return memo[n]
for _ in range(int(input())):
    Zcount,Ocount = 0,0
    print(*fibonacci(int(input())),sep=' ')