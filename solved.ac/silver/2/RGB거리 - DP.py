n = int(input())
dp = [{0:0},{0:0},{0:0}]
town = [[0,0,0]] + [list(map(int, input().split())) for _ in range((n))]
for i in range(1,n+1):
    dp[0][i] = min(dp[1][i-1], dp[2][i-1]) + town[i][0]
    dp[1][i] = min(dp[0][i-1], dp[2][i-1]) + town[i][1]
    dp[2][i] = min(dp[0][i-1], dp[1][i-1]) + town[i][2]
print(min([dp[0][n],dp[1][n],dp[2][n]]))
