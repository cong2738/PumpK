n = int(input())
for i in range(n):    
    score, tmp = 0, 0
    OX = input()
    for index in range(len(OX)):
        if OX[index] == 'O': tmp += 1
        else: tmp = 0
        score += tmp
    print(score)
