N = int(input())
M = int(input())
ing = list(map(int,input().split()))
ing.sort(reverse=True)

cnt,p1,p2 = 0,0,1

while ing[p1] + ing[p1+1] >= M:
    amor = ing[p1] + ing[p2]
    if amor >= M:
        cnt += (amor == M)
        p2 += 1
    else:
        p1 += 1
        p2 = p1+1

print(cnt)