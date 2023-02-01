def solution(land):
    n = len(land)
    land = land    
    dp = [{0:0},{0:0},{0:0},{0:0}]
    for i in range(1,n + 1):
        dp[0][i] = max([dp[1][i-1],dp[2][i-1],dp[3][i-1]]) + land[i-1][0]
        dp[1][i] = max([dp[0][i-1],dp[2][i-1],dp[3][i-1]]) + land[i-1][1]
        dp[2][i] = max([dp[1][i-1],dp[0][i-1],dp[3][i-1]]) + land[i-1][2]
        dp[3][i] = max([dp[1][i-1],dp[2][i-1],dp[0][i-1]]) + land[i-1][3]
    return max([dp[0][n],dp[1][n],dp[2][n],dp[3][n]])
print(solution([
    [1,2,3,5],
    [5,6,7,8],
    [4,3,2,1]
    ]))