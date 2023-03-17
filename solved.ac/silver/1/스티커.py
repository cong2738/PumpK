import sys
readline = sys.stdin.readline

for _ in range(int(readline())):
    n = int(readline())
    stickers = [list(map(int,readline().split())),
                list(map(int,readline().split()))]
    
    memo = [[0]*(n+1) for _ in range(2)] #각열에서 끝날떄의 최댓값을 저장할 memo
    
    #첫칸을 선택할 경우인 memo[][1]을 채워준다.
    memo[0][1] = stickers[0][0]
    memo[1][1] = stickers[1][0]

    #다른 열에서 두칸에서 끝나는 경우의 크기를 비교, 큰것을 선택.
    for i in range(2,n+1):
        memo[0][i] = max(memo[1][i-1],memo[1][i-2]) + stickers[0][i-1]
        memo[1][i] = max(memo[0][i-1],memo[0][i-2]) + stickers[1][i-1]
    print(max(memo[0][n],memo[1][n]))