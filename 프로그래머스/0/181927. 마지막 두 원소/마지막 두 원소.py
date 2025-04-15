def solution(num_list):
    l = len(num_list)
    L0 = num_list[l-2]
    L1 = num_list[l-1]
    
    return num_list + [L1 - L0 if L1 > L0 else L1*2]