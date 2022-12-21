input()
data = list(map(int,input().split()))
data_dict = {x:i for i,x in enumerate(sorted(set(data)))}
print(' '.join([str(data_dict[x]) for x in data]))