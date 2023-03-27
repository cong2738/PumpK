def solution(land):
    n,m =len(land), len(land[0])
    dp = [dict() for _ in range(m)]
    for i in range(n):
        dp[0] = min([dp[1][i-1],dp[2][i-1],dp[3][i-1]]) + land[i-1][1]
        dp[1]
        dp[2]
        dp[3]
    return 0
print(solution([
    [1,2,3,5],
    [5,6,7,8],
    [4,3,2,1]
    ]))