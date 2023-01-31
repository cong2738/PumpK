channel = input()
bkNum = int(input())
broken_bt = set(input().split())
minc,minc_cnt = '',0
for idx,cnum in enumerate(channel):
    if cnum in broken_bt: break
    minc += cnum
    minc_cnt += 1
for num in range(9,-1,-1):
    print(num)
    if not str(num) in broken_bt: break
print(num)