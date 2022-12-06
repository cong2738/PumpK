def solution(arr):
    arr.remove(min(arr))
    return  arr or [-1]
print(solution([1,2,3,4,5]))
