country = [input().split()]
game = {}
for i in range(6):
    A,B,winRate,drawRage,loseRate = input().split()
    game[(A,B)] = [winRate,drawRage,loseRate]