import sys
readline = sys.stdin.readline
mmlist = [readline().split() for _ in range(int(readline()))]
mmlist.sort(key=lambda x:x[1],reverse=True)
mmlist.sort(key=lambda x:x[0])
for mm in mmlist: print(*mm)