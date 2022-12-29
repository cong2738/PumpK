import sys
readline = sys.stdin.readline
triangle = list()
for _ in range(int(readline())):
    triangle.append(list(map(int,readline().split())))

for f in range(len(triangle)-2,-1,-1):
    for idx in range(len(triangle[f])):
        triangle[f][idx] += max(triangle[f+1][idx],triangle[f+1][idx+1])
print(triangle[0][0])