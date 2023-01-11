import sys
from string import ascii_uppercase as au

alp = au.replace('J','')
readline = sys.stdin.readline
origin = readline().rstrip()
key_map = dict()
key_board = [['0']*5 for _ in range(5)]

idx = 0
for c in readline().rstrip()+alp:
    if c in key_map: continue
    key_map[c] = (idx//5,idx%5)
    key_board[idx//5][idx%5] = c
    idx += 1

trans = []
idx = 0
while idx < len(origin):
    if len(origin) - idx == 1: 
        trans.append(origin[idx]+'X')
        break
    elif origin[idx] != origin[idx+1]:
        trans.append(origin[idx:idx+1+1])
        idx+=2
    elif origin[idx] == origin[idx+1]:
        trans.append(origin[idx]+('X' if origin[idx] != 'X' else 'Q'))
        idx+=1

res = ''
for a,b in trans:
    (alow,acol),(blow,bcol) = map(lambda c:key_map[c],(a,b))
    if key_map[a][0] == key_map[b][0]:
        a = key_board[alow][(acol+1)%5]
        b = key_board[blow][(bcol+1)%5]
    elif key_map[a][1] == key_map[b][1]:
        a = key_board[(alow+1)%5][acol]
        b = key_board[(blow+1)%5][bcol]
    elif key_map[a][0] != key_map[b][0] and key_map[a][1] != key_map[b][1]:
        a = key_board[alow][bcol]
        b = key_board[blow][acol]
    res += a+b
    
print(res)