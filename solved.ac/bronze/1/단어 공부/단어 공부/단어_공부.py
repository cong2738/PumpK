
s = input().upper()
ret = list()
for c in set(s):
    ret.append([s.count(c),c])
ret.sort(reverse = True)
if len(ret) != 1 and ret[0][0] == ret[1][0]: print('?')
else: print(ret[0][1])