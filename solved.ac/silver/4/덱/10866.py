import sys
n = int(sys.stdin.readline())
DQ = list()
for i in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push_front": DQ = [cmd[1]] + DQ
    elif cmd[0] == "push_back": DQ += [cmd[1]]
    elif cmd[0] == "pop_front": print(DQ.pop(0) if DQ else -1)
    elif cmd[0] == "pop_back": print(DQ.pop(-1) if DQ else -1)
    elif cmd[0] == "size": print(len(DQ))
    elif cmd[0] == "empty": print(0 if DQ else 1)
    elif cmd[0] == "front": print(DQ[0] if DQ else -1)
    elif cmd[0] == "back": print(DQ[-1] if DQ else -1)