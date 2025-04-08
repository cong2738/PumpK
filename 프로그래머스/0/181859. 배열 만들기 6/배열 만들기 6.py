def solution(arr):
    stk = []
    for n in arr:
        if stk and stk[-1]  == n: stk.pop()
        else: stk.append(n)
    return stk if stk else [-1]