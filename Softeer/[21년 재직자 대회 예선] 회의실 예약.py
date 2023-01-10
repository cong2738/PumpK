import sys
readline = sys.stdin.readline
N,M = map(int,readline().split())
Room = {readline().rstrip():[] for _ in range(N)}
for _ in range(M): 
    name,*time = readline().split()
    time = list(map(int,time))
    Room[name].append(time)
ee = lambda x: x if len(x) == 2 else ('0'+x)
for name,times in Room.items(): 
    start = 9
    temp = []
    for st,ed in sorted(times): 
        if not(st <= start < ed): 
            temp.append(f'{ee(str(start))}-{ee(str(st))}\n')
        start = ed
    if start < 18: temp.append(f'{ee(str(start))}-18\n')
    Room[name] = temp
print('-----\n'.join(
        [f'Room {name}:\n'+(f'{len(times)} available:\n' if times else 'Not available\n')+''.join(times)  
        for name,times in sorted(Room.items(),key=lambda x:x[0])]
    )
)