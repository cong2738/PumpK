import re
def solution(str1, str2):
    answer = 0
    str1 = re.sub('[^a-zA-Z0-9]','',str1).upper()
    str2 = re.sub('[^a-zA-Z0-9]','',str2).upper()
    print(str1,str2)
    l1=[]
    l2=[]
    for x in range(0,len(str1)-1):
        l1.append(str1[x:x+2])
    for x in range(0,len(str2)-1):
        l2.append(str2[x:x+2])
    s1 = set(l1)
    s2 = set(l2)
    print(s1,s2)
    jakad = len(s1&s2)/len(s1|s2)
    answer = int(jakad*65536)
    return answer
print(solution("FRANCE", "french"))
