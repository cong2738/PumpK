import sys
readline = sys.stdin.readline

using = set()
def seat():
    ret = (0,float('inf'),float('inf'))
    if not using: return (0,0,0)
    for x in range(N):
        for y in range(M):
            stab = float('inf')
            for sx,sy in using:
                temp = (sx-x)**2 + (sy-y)**2
                stab = min(stab,temp)
            if stab <= 1 or stab == float('inf'): continue
            ret = min(ret,(-stab,x,y))
    return ret if ret[1] != float('inf') and ret[2] != float('inf') else False

N,M,Q = map(int,readline().split())
board = [[0]*M for _ in range(N)]
eat = set()
leave = set()
employee = dict()
for _ in range(Q):
    cmd,id = readline().split()
    if cmd == 'In':        
        if id in leave: print(f'{id} already ate lunch.')
        elif id in eat: print(f'{id} already seated.')
        else:  
            try: _,x,y = seat()
            except: 
                print('There are no more seats.')
                continue
            eat.add(id)
            using.add((x,y))
            employee[id] = (x,y)
            print(f'{id} gets the seat ({x+1}, {y+1}).')
    elif cmd == 'Out':
        if id not in eat: print(f'{id} didn\'t eat lunch.')
        elif id in leave: print(f'{id} already left seat.')
        else:
            x,y = employee[id]
            print(f'{id} leaves from the seat ({x+1}, {y+1}).')
            using -= {employee[id]}
            leave.add(id)