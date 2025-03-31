def solution(code):
    mode = 0
    ret = ""
    for i,c in enumerate(code):
        if(c=="1"):
            mode = 0 if mode else 1 
        elif not mode:
            ret += "" if i % 2 else c
        else:
            ret += c if i % 2 else ""
            
    return ret if ret else "EMPTY"