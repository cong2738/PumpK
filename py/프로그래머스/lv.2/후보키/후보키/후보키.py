from itertools import combinations
def solution(relation):
    tag = ['snum','name','class','grade']
    comb = [[0],[1],[2],[3]] + list(combinations([0,1,2,3],2)) + list(combinations([0,1,2,3],3)) + list(combinations([0,1,2,3],4))
    ck = []
    ret = []
    for data in comb:
        uni = set()
        for person in relation:
            uni.add(tuple([person[x] for x in data]))
        if len(uni)==len(relation):
            tmp =tuple([tag[x] for x in data])
            ck.append(tmp)
    ck.sort(key=lambda x:len(x))
    for i in ck:
        find = False
        for j in ret:
            if(str(j)[1:-1] in str(i)):
                find = True
                break
        if(not find):
            ret.append(i)
    print(*ret,sep ='\n')
    return len(ret)
rel = [
    ["100","ryan","music","2"],
    ["200","apeach","math","2"],
    ["300","tube","computer","3"],
    ["400","con","computer","4"],
    ["500","muzi","music","3"],
    ["600","apeach","music","2"]
       ]
print(solution(rel))
