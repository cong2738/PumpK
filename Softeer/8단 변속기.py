nums =  list(map(int, input().split()))
step = nums[1] - nums [0]
for i in range(len(nums) - 1):
    if step != nums[i+1] - nums[i]: step = 0; break
if not step: print('mixed')
elif step == -1: print('descending')
else: print('ascending')