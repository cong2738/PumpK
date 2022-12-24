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
for _ in range(n):
    line = list(map(int,readline().split()))
    parent = line[0]
    tmp = dict()
    for i in range(1,len(line)-1,2):
        tmp[line[i]] = line[i+1]
    tree[parent] = tmp

fd = find(n,tree)
fd.start_dfs(1,n)
distance = fd.get_distance()
start = distance.index(max(distance))
fd.start_dfs(start,n)
distance = fd.get_distance()
print(max(distance))