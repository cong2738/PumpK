import sys
readline = sys.stdin.readline
sys.setrecursionlimit(100000)

N = {-1:0,0:0,1:0}
slicePaper = lambda pap,x,y,dx,dy: [line[x:x+dx] for line in pap[y:y+dy]]
def is_OK(pap):
    zero = pap[0][0]
    for line in pap:
        for num in line:
            if num != zero: return 10
    return zero
def cut(pap):
    cutsize = len(pap) // 3
    OK = is_OK(pap)
    if  OK in N:
        N[OK] += 1
        return
    for x in range(3):
        for y in range(3):
            newpaper = slicePaper(pap,x*cutsize,y*cutsize,cutsize,cutsize)
            cut(newpaper)

paper = [list(map(int,readline().split())) for _ in range(int(readline()))]
cut(paper)
print(*N.values(),sep='\n')