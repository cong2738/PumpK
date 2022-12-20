input_num = int(input())
n = 3
memo = [0,0,1,1] + [0]*(10**6)
while(input_num > 3 and n != input_num):
    n += 1
    ps_memolist = [memo[n-1]]
    if n%3 == 0: ps_memolist.append(memo[n//3])
    if n%2 == 0: ps_memolist.append(memo[n//2])
    memo[n] = min(ps_memolist) + 1
print(memo[input_num])
