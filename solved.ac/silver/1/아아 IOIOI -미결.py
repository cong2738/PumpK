def kmp(text, target):
    #kmp_table
    table = [0 for _ in range(len(target))]
    i = 0
    for j in range(1, len(target)):
        while i > 0 and target[i] != target[j]:
            i = table[i - 1]
        if target[i] == target[j]:
            i += 1
            table[j] = i
    #kmp
    result = []
    i = 0
    for j in range(len(text)):
        while i > 0 and target[i] != text[j]:
            i = table[i-1]
        if target[i] == text[j]:
            i += 1
            if i == len(target):
                result.append(j-i+1)
                i = table[i-1]
    return result

N = int(input())
M = int(input())
IOI = 'I' + 'OI'*N
print(len(kmp(input(), IOI)))