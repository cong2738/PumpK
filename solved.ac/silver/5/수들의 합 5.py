n = int(input())

start = end = s = cnt = 1

while start != n:
    print(start,end,s)
    if s == n:
        end += 1
        cnt += 1
        s += end
    elif s > n:
        s -= start
        start += 1
    else: 
        end += 1
        s += end

print(cnt)