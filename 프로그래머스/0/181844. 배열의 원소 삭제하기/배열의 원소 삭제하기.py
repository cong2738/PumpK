def solution(arr, delete_list):
    for d in delete_list:
        if(d not in arr): continue
        arr.remove(d)
    return arr