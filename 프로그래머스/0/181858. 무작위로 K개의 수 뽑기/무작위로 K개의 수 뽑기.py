def solution(arr, k):
    temp = dict()
    for n in arr:
        temp[n] = 0
    answer = list(temp.keys())[0:k]
    return answer + [-1]*(k-len(answer))