def solution(s, n):
    ret =''
    for c in s:
        if c.isupper():
            ret += chr(ord('A')+(ord(c)-ord('A')+n)%26)
        elif c.islower():
            ret += chr(ord('a')+(ord(c)-ord('a')+n)%26)
        else:
            ret+=c
    return ret
print(solution('AB',1))
