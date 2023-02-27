import sys
readline = sys.stdin.readline

#가독성을 위해 ng는 z로 치환해서 디코드한다.
minAlp = {key:value for key,value in zip("a b k d e g h i l m n z o p r s t u w y".split(),range(20))} 
minDict = dict()
for _ in range(int(readline())):
    word = readline().rstrip()
    temp = word.replace('ng','z')
    code = [minAlp[c] for c in temp]
    minDict[word] = code

print(*sorted(minDict, key=lambda x:minDict[x]), sep='\n')