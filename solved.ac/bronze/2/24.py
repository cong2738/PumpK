def decode(timestring):
    sec = 0
    for i,t in zip([60*60,60,1],list(map(int,timestring.split(':')))):
        sec += i*t
    return sec
def encode(sec):
    ret = ''
    for _ in range(3):    
        time = str(sec%60)
        if len(time) != 2: time = '0'+time
        ret =  time + ':' + ret
        sec //= 60
    return ret[:-1]
a,b = decode(input()),decode(input())
if b < a: b += 24*60*60
print(encode(b-a))