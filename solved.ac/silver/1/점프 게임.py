import sys
from collections import deque
readline = sys.stdin.readline
global visited, move, bridge, N, k
def bfs():
    visited = set([''])
    q = deque([([0,0],'')])
    while q:
        loc,data = q.popleft()
        line, loc = loc
        if loc >= N: return 1
        for m, cmd in move:
            nxt = data + cmd
            nline, nloc = m(line, loc)
            if not nxt in visited  and bridge[nline][nloc] and len(data) <= loc:
                q.append(([nline,nloc],nxt))
                visited.add(nxt)
    return 0

N,k = map(int,readline().split())
move = [
    [lambda line,loc:[line,loc+1], 'F'],
    [lambda line,loc:[line,loc-1], 'B'],
    [lambda line,loc:[(line+1)%2,loc+k], 'C']]
left = list(map(int,readline().rstrip())) + [1]*k
right = list(map(int,readline().rstrip())) + [1]*k
bridge = [left,right]
print(bfs())