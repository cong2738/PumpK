def solution(arr1, arr2):
    ret = arr1
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            ret[i][j]=arr1[i][j]+arr2[i][j]
    return ret
