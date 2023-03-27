import heapq as hq

def solution(food_times, K):
    hq.heapify(food_times)
    n = len(food_times)

    for cnt in range(n):
        if len(food_times) == 1 or food_times[0] >= K: break
        hq.heappush(food_times, hq.heappop(food_times) + 2*hq.heappop(food_times))

    return cnt if food_times[0] >= K else -1