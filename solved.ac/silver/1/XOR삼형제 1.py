import sys
readline = sys.stdin.readline
for _ in range(int(readline())):
    N = XOR = int(readline())
    ret = set()
    for i in range(1,N+1):
        tmp = [i]
        for j in range(1,N+1):
            if i^j == 0 or i^j > N: ret.add(i)
            print(i,j,i^j)
    print(*ret)
print(1^2^3)