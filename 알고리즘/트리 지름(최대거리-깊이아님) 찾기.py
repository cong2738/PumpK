import sys
readline = sys.stdin.readline

class find:
    distance = list()
    num = 0
    tree = dict()

    def __init__(self,num,tree):
        self.num = num
        self.tree = tree

    sys.setrecursionlimit(100000)        
    def __dfs(self,p,dia):
        for np in self.tree[p]:
            if self.distance[np] == -1: 
                self.distance[np] = dia + self.tree[p][np]
                self.__dfs(np, self.distance[np])

    def start_dfs(self,start,num):
        self.distance = [-1] * (num + 1)
        self.distance[start] = 0
        self.__dfs(start, 0)

    def get_distance(self): 
        return self.distance

#입력
n = int(readline())
tree = {i:dict() for i in range(1,n+1)}
for _ in range(n):
    line = list(map(int,readline().split()))
    parent = line[0]
    tmp = dict()
    for i in range(1,len(line)-1,2):
        tmp[line[i]] = line[i+1]
    tree[parent] = tmp

'''
트리(tree)는 사이클이 없는 무방향 그래프이다. 
트리에서는 어떤 두 노드를 선택해도 둘 사이에 경로가 항상 하나만 존재하게 된다. 
트리에서 어떤 두 노드를 선택해서 양쪽으로 쫙 당길 때, 가장 길게 늘어나는 경우가 있을 것이다. 
이럴 때 트리의 모든 노드들은 이 두 노드를 지름의 끝 점으로 하는 원 안에 들어가게 된다.
'''
# 꼬리탐색(임의의 A점으로부터 가장 먼 위치)
fd = find(n,tree)
fd.start_dfs(1,n)
distance = fd.get_distance()
# 꼬리로부터 가장먼(머리)탐색
start = distance.index(max(distance))
fd.start_dfs(start,n)
distance = fd.get_distance()
print(max(distance))