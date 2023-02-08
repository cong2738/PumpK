import sys
from collections import deque
readline = sys.stdin.readline
employee = lambda x:[deque([]),dict()] # 직원의 기본구조

#root에 h깊이의 트리 생성, h**2개의 이파리가 생기므로 h**2줄의 공백으로 구분된 k개의 task입력을 받음
def maketree(depth,node):
    #해당 노드가 이파리(트리의 끝)인 경우 tasks저장및 종료
    if depth == 0: 
        node[0] = deque(map(int,readline().split()))
        return
    #부하 두명 저장
    node[1][0] = employee('R')
    node[1][1] = employee('L')
    #만들어진 좌우부하에서도 동일하게 루트 분할
    maketree(depth-1,node[1][0])
    maketree(depth-1,node[1][1])

'''
깊이우선
 직원은 하위 직원에게서 task를 받아옴. 
짝수일에는 오른쪽 홀수일에는 왼쪽직원의 left task pop. 
하위 두 직원으로 분기하여 재귀하며 최하위직원일때 재귀중단
'''
def work(depth,node,RL):
    #이파리(트리의끝)인경우 재귀 종료
    if depth == 0: return
    #현재 타겟(RL)의 부하직원의 태스크를 하나 빼서 자기태스크에 넣는다
    if node[1][RL][0]:
        node[0].append(node[1][RL][0].popleft())
    #부하직원 좌 우에대해서 다시 재귀
    work(depth-1,node[1][0],RL)
    work(depth-1,node[1][1],RL)

h,k,r = map(int,readline().split()) #트리의 깊이h, 태스크의 개수 k, 날짜 r
tree = employee('root') #직원의 기본구조를 가진 root생성
maketree(h,tree) 
for date in range(1,r): 
    work(h,tree,(date)%2)
print(sum(tree[0]))