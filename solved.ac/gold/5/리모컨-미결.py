channel = input()
bkNum = int(input())
broken_bt = input().split()
justPM_Push = abs(int(channel)-100)
push = 0
user_chanel = []
for num in channel:
    push += 1
    if not num in broken_bt:
        user_chanel.append(num)        
    else:
        user_num = 0
        for i in range(10):
            if not i in broken_bt:
                user_num = min(user_num,i,key=lambda x:int(num)-x)
        user_chanel.append(str(user_num))
user_chanel = ''.join(user_chanel)
push += abs(int(channel) - int(user_chanel))
print(push,justPM_Push)