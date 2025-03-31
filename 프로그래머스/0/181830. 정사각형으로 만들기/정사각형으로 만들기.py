def solution(arr):
    r, c = len(arr), len(arr[1])
    if c >= r:
        answer = arr
        answer += [[0]*c]*(c-r)
    else:
        answer = []
        for row in arr:
            answer.append(row+[0]*(r-c))
    return answer