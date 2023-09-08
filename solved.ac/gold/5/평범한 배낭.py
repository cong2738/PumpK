import sys
readline = sys.stdin.readline

def knapsck(limit:int,item_list):
    # 가방의 해당 가치에대한 무게의 최소값 해시맵 
    bag = {0:0} # {가치:무게}

    for w_in,v_in in item_list:
        tmp = {} # 중간에 해시맵 크기가 늘어나면 안되니 업데이트 할 데이터를 저장해놓을 tmp

        # 무게가 작은 조합을 선정 해당 가치표에 작성한다.
        for v_bag,w_bag in bag.items():
            if (w_sum := w_bag + w_in) < bag.get(v_sum := v_bag + v_in, limit+1):
                tmp[v_sum] = w_sum
        
        bag.update(tmp) # 가방의 [가치-무게]표 정보 업데이트

    return max(bag.keys()) # 가능한 최고 가치를 반환(무게는 신경안쓴다)

N,K = map(int,readline().split())
items = [list(map(int,readline().split())) for _ in range(N)]
items.sort(reverse=True)

print(knapsck(K,items))