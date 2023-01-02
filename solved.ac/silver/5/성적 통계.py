import sys
readline = sys.stdin.readline
for i in range(1,int(readline())+1):    
    MaxGap, N, *data = 0, map(int, readline().split())
    data.sort()
    for j in range(N-1): MaxGap = max(MaxGap, data[j+1]-data[j])
    print(f'Class {i}\nMax {data[-1]}, Min {data[0]}, Largest gap {MaxGap}')