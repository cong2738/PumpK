import sys
n = int(sys.stdin.readline())
Q = list()
for line in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push": Q.append(cmd[1])
    elif cmd[0] == "pop": print(Q.pop(0) if Q else -1)
    elif cmd[0] == "size": print(len(Q))
    elif cmd[0] == "empty": print(0 if Q else 1)
    elif cmd[0] == "front": print(Q[0] if Q else -1)
    elif cmd[0] == "back": print(Q[-1] if Q else -1)