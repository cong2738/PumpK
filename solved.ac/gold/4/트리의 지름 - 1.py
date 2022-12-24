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


n = int(readline())
tree = {i:dict() for i in range(1,n+1)}
#set_tree
for _ in range(n-1):
    p,c,d = map(int,readline().split())
    tree[p][c] = d
    tree[c][p] = d
Fd = find(n,tree) 

# 1번 노드에서 가장 먼 곳을 찾는다.
Fd.start_dfs(1,n)
Distance = Fd.get_distance()

# 위에서 찾은 노드에 대한 가장 먼 노드를 찾는다.
start = Distance.index(max(Distance))
Fd.start_dfs(start, n)
Distance = Fd.get_distance()

print(max(Distance))
