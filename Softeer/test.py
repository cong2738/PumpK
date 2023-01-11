def et(string,*L):
    for s in L:
        string = string.replace(s,'')
    return string
item_option  = [(lambda s:[s[0].split(':'),s[1]])(et(s,'value\': ', 'grade\': ', '\'', '{', '}',' ').split(',')) for s in [s for s in input().split('}, ')]]
print(*item_option, sep='\n')