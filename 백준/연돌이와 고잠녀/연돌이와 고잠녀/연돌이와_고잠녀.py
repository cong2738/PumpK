n,m = input().split();
road = [[],[]]
for i in range(int(n)): 
    road[0].append([float(i) for i in input().split()])
for i in range(int(m)): 
    road[1].append([float(i) for i in input().split()])
