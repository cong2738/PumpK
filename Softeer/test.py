def et(string,*L):
    for s in L:
        string = string.replace(s,'')
    return string
item_option  = [et(s,'value\': ', 'grade\': ', '\'', '{', '}') for s in [s for s in input().split('}, ')]]
print(*item_option, sep='\n')