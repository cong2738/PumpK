N = int(input())
nums = list(map(int,input().split()))

res = float('INF')
p1,p2 = 0,0

for i in range(N-1):
    current = nums[i]

    start = i + 1
    end = N - 1

    while start <= end:
        mid = (start + end) // 2
        tmp = current + nums[mid]

        if abs(tmp) < res:
            res = abs(tmp)
            p1 = i
            p2 = mid

            if tmp == 0: break

        if tmp < 0: start = mid + 1
        else: end = mid - 1        

print(nums[p1],nums[p2])