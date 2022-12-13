
n = int(input())
for i in range(n):
    rpt, s = input().split()
    ret = ""
    for c in s:
        ret += c*int(rpt)
    print(ret)