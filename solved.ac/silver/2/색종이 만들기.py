import sys
input = sys.stdin.readline

def allColor(paper):
    color = paper[0][0]
    for line in paper:
        for tmp_color in line:
            if color != tmp_color:
                return False
    return True
    
cnt = [0,0]
def slice(paper):
    global cnt
    if allColor(paper):
        cnt[paper[0][0]] += 1
        return cnt
    d = len(paper)//2
    p = [[0,0],[0,1],[1,0],[1,1]]
    for coex,coey in p:
        x, y = coex * d, coey * d
        slice([line[x:x+d] for line in paper[y:y+d]])

paper = [list(map(int,input().split())) for _ in range(int(input()))]
OK = True
slice(paper)
print(*cnt,sep='\n')