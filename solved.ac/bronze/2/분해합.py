input_num = int(input())
for num in range(input_num//2, input_num):
    if num + sum([int(i) for i in str(num)]) == input_num: 
        print(num)
        break
else: print(0)