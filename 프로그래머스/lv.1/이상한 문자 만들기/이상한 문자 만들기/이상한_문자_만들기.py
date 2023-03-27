def solution(s):
    ret = []
    for i in s.split(' '):
        word = ''
        for j in range(len(i)):
            if j%2==0:
                tmp = list(i)[j].upper()
            else:
                tmp = list(i)[j].lower()
            word += tmp
        ret.append(word)
    return ' '.join(ret)
print(solution('abc cde'))
