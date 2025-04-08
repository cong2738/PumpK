def solution(arr, k):
    answer = []
    i = 0
    while len(answer) < k and i < len(arr):
        if arr[i] not in answer:
            answer.append(arr[i]) 
        i+=1
            
    if len(answer) < k: answer+=[-1]*(k-len(answer))
    return answer