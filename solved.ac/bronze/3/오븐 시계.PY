time = (lambda x:60*int(x[0]) + int(x[1]))(input().split()) + int(input())
print(time // 60 % 24, time % 60)
