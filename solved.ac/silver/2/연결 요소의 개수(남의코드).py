import sys
readline = sys.stdin.readline

nodes = dict()
nets = dict()
n,m = map(int,readline().split())

for i in range(n):
    nodes[i+1] = i
    nets[i] = [i+1]
for _ in range(m):
    a,b = map(int,readline().split())
    if nodes[a] != nodes[b]:
        high,low = nodes[a],nodes[b] if nodes[a] > nodes[b] else nodes[b],nodes[a]
        for i in nets[high]:
            nodes[i] = low
            nets[low].append(i)
        del nets[high]
    print(len(nets))
