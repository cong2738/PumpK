import sys
input = sys.stdin.readline
for T in range(int(input())):
    Q = list()
    for k in range(int(input())):
        cmd = input().split()
        if cmd[0] == 'I':
            Q.append(int(cmd[1]))
            Q.sort()
        elif cmd[0] == 'D' and Q:
            if cmd[1] == '-1':
                del Q[-1]
            elif cmd[1] == '1':
                del Q[0]
    if Q: print(max(Q),min(Q))
    else: print('EMPTY')
