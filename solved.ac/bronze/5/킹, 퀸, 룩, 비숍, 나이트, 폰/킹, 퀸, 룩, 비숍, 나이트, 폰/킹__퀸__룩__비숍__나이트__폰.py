chess = [1,1,2,2,2,8]
have = list(map(int,input().split()))
for ret in zip(chess,have):
    print(ret[0]-ret[1],end=' ')