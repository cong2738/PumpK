import sys
readline = sys.stdin.readline
N,M = map(int,readline().split())
Room = {readline().rstrip():[] for _ in range(N)}
for _ in range(M):
    name,*time = readline().split()
    time = list(map(int,time))
    Room[name].append(time)
eeee = lambda x:x if len(x) == 2 else ('0'+x)
for name,times in Room.items():
    start = 9
    res = []
    for st,ed in sorted(times):
        if st <= start < ed: start = ed; continue        
        res.append(f'{eeee(str(start))}-{eeee(str(st))}\n')
        start = ed
    if start < 18: res.append(f'{eeee(str(start))}-18\n')
    Room[name] = res
print('-----\n'.join(
    [f'Room {name}:\n'+
    (f'{len(times)} available:\n' if times else 'Not available\n')+
    ''.join(times) for name,times in sorted(Room.items(),key=lambda x:x[0])]
    ))
