import sys
readline = sys.stdin.readline

def knapsck(limit:int,item_list):
    bag = {0:0} # {가치:리스크}

    for w_in,v_in in item_list:
        tmp = {}

        for v_bag,w_bag in bag.items():
            w_sum = w_bag + w_in
            if w_sum < 100 and w_sum < bag.get(v_sum := v_bag + v_in, limit+1):
                tmp[v_sum] = w_sum
        
        bag.update(tmp) 

    return max(bag.keys())


_ = int(readline())
pain = list(map(int,readline().split()))
pleasure = list(map(int,readline().split()))
p = list(zip(pain,pleasure))

print(knapsck(100,p))