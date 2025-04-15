def solution(my_string, s, e):
    s1 = my_string[:s]
    s2 = "".join(reversed(list(my_string[s:e+1])))
    s3 = my_string[e+1:]
    
    return s1+s2+s3