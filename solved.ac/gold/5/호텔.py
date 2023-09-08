import sys

readline = sys.stdin.readline

def knapsck(goal:int,city_list):
    dp = [0] + [float('inf')]*(goal+101)

    for cost,value in city_list:
        for i in range(value,goal+100):
            dp[i] = min(dp[i],dp[i-value]+cost)

    return min(dp[goal:])

def input_data():
    C,N = map(int,readline().split())

    # [[cost,value],...]
    city = [list(map(int,readline().split())) for _ in range(N)]    

    return C,city    

if __name__ != '__main__': quit()

print(knapsck(*input_data()))