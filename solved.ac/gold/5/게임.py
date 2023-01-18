from collections import deque
import sys
readline = sys.stdin.readline
import time

start = time.time()

S = 500 + 1
board = [['S']*S for _ in range(S)]
for _ in range(int(readline())):
    X1,Y1,X2,Y2 = map(int,readline().split())
    for x in range(min(X1,X2),max(X1,X2)+1):
        for y in range(min(Y1,Y2),max(Y1,Y2)+1):
            board[y][x] = 'W'
for _ in range(int(readline())):
    X1,Y1,X2,Y2 = map(int,readline().split())
    for x in range(min(X1,X2),max(X1,X2)+1):
        for y in range(min(Y1,Y2),max(Y1,Y2)+1):
            board[y][x] = 'D'


end = time.time()
print(f"{end - start:.5f} sec")
'''
첫째 줄에 위험한 구역의 수 N이 주어진다. 
다음 줄부터 N개의 줄에는 X1 Y1 X2 Y2와 
같은 형식으로 위험한 구역의 정보가 주어진다. 
(X1, Y1)은 위험한 구역의 한 모서리이고, 
(X2, Y2)는 위험한 구역의 반대 모서리이다. 
그 다음 줄에는 죽음의 구역의 수 M이 주어진다. 
다음 줄부터 M개의 줄에는 죽음의 구역의 정보가 
위험한 구역의 정보와 같이 주어진다. 
주어지는 구역은 모두 겹칠 수 있으며, 
서로 다른 구역이 겹칠 때는, 더 심한 구역이 해당된다. 
예를 들어, 
죽음+위험 = 죽음, 
위험+안전 = 위험, 
위험+위험 = 위험, 
죽음+안전 = 죽음이다. 
위험한 구역이 아무리 겹쳐도 생명은 1씩 감소된다. 
생명의 감소는 구역에 들어갈 때만, 영향을 미친다. 
예를 들어, (500, 500)이 위험한 구역일 때는, (500, 500)에 들어갈 때, 
생명이 1 감소되지만, (0, 0)이 위험한 구역이더라도 생명은 감소되지 않는다. 
마찬가지로, (0, 0)이 죽음의 구역이더라도 
세준이는 이미 그 곳에 있으므로 세준이에게 영향을 미치지 않는다. 
N과 M은 50보다 작거나 같은 자연수이다.
'''