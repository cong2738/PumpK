
n,m=map(int,input().split())
low_guard = [0 for i in range(n)]
col_guard = [0 for i in range(m)]
for y in range(n):
    floor = input()
    for x in range(m):
        if floor[x]=='X':
            low_guard[y]=1
            col_guard[x]=1
print(max(low_guard.count(0),col_guard.count(0)))
