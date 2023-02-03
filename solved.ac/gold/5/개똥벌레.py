import sys
readline = sys.stdin.readline
N,H = map(int,readline().split())
b,t = list(),list()
for _ in range(N//2):
    b.append(int(readline()))
    t.append(int(readline()))
b.sort(),t.sort()
print(b)
print(t)