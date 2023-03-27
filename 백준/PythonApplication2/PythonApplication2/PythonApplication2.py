S = int(input())
add, num ,count = 0, 0, 0
while(add <= S):
    num += 1
    add += num
    count+=1
print(count - 1)
