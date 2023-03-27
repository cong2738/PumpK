from gettext import find
def solution(msg):
    answer = []
    alph = {"":0,"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
    index = 0
    while (alph!=''):
        word = ''
        print(word in alph)
        while ((len(alph)!=0) and ((word in alph)==True)):
            print('s')
            word += msg[0]
            msg=msg[1:]
        alph[word]=len(alph)
    print(alph)
    if(len(msg)%2==1): 
        answer.append(alph[msg[-1]])
    return answer
print(solution("KAKAO"))
## 씨발 C++로 돌아갈래