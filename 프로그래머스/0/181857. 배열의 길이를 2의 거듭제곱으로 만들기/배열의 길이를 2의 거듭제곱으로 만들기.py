def solution(arr):
    target,n = 1,len(arr);
    while(target < n):
        target*=2
    return arr + [0]*(target-n)