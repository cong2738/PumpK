def solution(arr):
    stk = []
    for i,n in enumerate(arr):
        if stk and stk[-1]  == arr[i]: stk.pop()
        else: stk.append(n)
    return stk if stk else [-1]