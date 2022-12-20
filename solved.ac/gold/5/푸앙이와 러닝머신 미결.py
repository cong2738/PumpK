import math
bts = [8, 4, 1]
def maxpush(Dis):
    maxpustime = 0
    for bt in bts:
        maxpustime += Dis//bt        
        Dis %= bt
    return maxpustime

def solution():    
    D, T = map(int,input().split())
    res_time = 0
    if  maxpush(D) > T:
        print(-1)
        return
    for bt in bts:
        ontime = D//bt
        if D%bt == 0 and ontime < T: 
            print(T-ontime, bt)
            return
    while D != 0:
        bt_times = [[8,math.inf], [4,math.inf], [1,math.inf]]
        for bt in range(3):
            tmp = D//bts[bt]     
            if D%bts[bt] == 0 and ontime < T: 
                print(T-ontime, bts[bt])
                return  
            if tmp != 0: bt_times[bt][1] = tmp
        mb = min(bt_times, key=lambda x:x[1])        
        D -= mb[0] * mb[1]            
        print(res_time, mb[0])
        res_time += mb[1]    

solution()