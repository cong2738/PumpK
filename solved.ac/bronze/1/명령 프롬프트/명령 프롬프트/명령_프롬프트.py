n = int(input())
cmds = [list(input()) for s in range(n)]
bc = cmds[0]
for i in range(1,len(cmds)):
    for j in range(len(cmds[i])):
        if not bc[j]==cmds[i][j]:
            bc[j]='?'
print(''.join(bc))
