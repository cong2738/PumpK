A,B = map(int,input().split())
num = []
for i in range(1,B+1):
    num += [i]*i
print(sum(num[A-1:B]))