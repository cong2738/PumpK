from functools import reduce

mult = lambda x,y : x * y
input_num = input()
front, back = 1, -1
for index in range(1,len(input_num)):
    front = reduce(mult,list(map(int,input_num[:index])))
    back = reduce(mult,list(map(int,input_num[index:])))
    if(front == back): break
if front == back: print("YES")
else: print("NO")