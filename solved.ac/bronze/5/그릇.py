ret = 0
plates = input()
backplate = ''
for dish in plates:
    if backplate == dish: ret += 5
    else: 
        backplate = dish
        ret += 10    
print(ret)