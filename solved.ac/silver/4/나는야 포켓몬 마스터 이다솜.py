import sys
readline = sys.stdin.readline
n,m = map(int,readline().split())
num_p = {num:readline().strip() for num in range(1,n+1)}
p_num = {name:num for num,name in num_p.items()}
ret_list = []
for _ in range(m):
    Q = readline().strip()
    if Q in p_num: ret_list.append(p_num[Q])
    elif int(Q) in num_p: ret_list.append(num_p[int(Q)])
print(*ret_list,sep='\n')
