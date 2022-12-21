N = int(input())
M = int(input())
S = input()
cnt = 0
tmp = S[0]
for i in range(M):
    if tmp[0] == 'I': 
        if tmp[-1] != S[i]:
            tmp += S[i]
        else: 
            cnt += tmp.count('O') - N + 1
            tmp = S[i]
    else: tmp = S[i]
if tmp[0] != "O" and tmp[-3:] == "IOI": cnt += tmp.count('O') - N + 1
print(cnt)