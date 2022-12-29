from sys import stdin
readline = stdin.readline
p, m = 0, 0
for _ in range(4):
    o, i = map(int,readline().split())
    p += i - o
    m = max(m,p)
print(m)