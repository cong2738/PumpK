memo = {0:1,1:1,2:2}
def OneToThree(n):
    global memo
    if not n in memo: memo[n] = OneToThree(n-1) + OneToThree(n-2) + OneToThree(n-3)
    return memo[n]
for _ in range(int(input())): print(OneToThree(int(input())))