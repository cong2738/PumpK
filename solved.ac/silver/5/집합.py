import sys
input = sys.stdin.readline
S = set()
ret = list()
for _ in range(int(input())):
    cmd = input().split()    
    if cmd[0] == 'add': S.add(int(cmd[1]))
    elif cmd[0] == 'remove' and int(cmd[1]) in S: S.remove(int(cmd[1]))
    elif cmd[0] == 'check': print(1 if int(cmd[1]) in S else 0)
    elif cmd[0] == 'toggle': S.remove(int(cmd[1])) if int(cmd[1]) in S else S.add(int(cmd[1]))
    elif cmd[0] == 'all': S = {i + 1 for i in range(20)}
    elif cmd[0] == 'empty': S.clear()