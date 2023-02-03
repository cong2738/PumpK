origin = [ord(c) for c in input()]
vigenere = [ord(c) for c in input()]
keyline = ''
for o,v in (zip(origin,vigenere)):
    k = v - o
    if k < 0: k += 26
    keyline += chr(ord('A')+k-1)
key = keyline
size = len(keyline)
for keylen in range(1,size+1):
    if size%(keylen): continue    
    flag = {keyline[i*keylen:(i+1)*keylen] for i in range(size//keylen)}
    if len(flag) == 1:
        key = list(flag)[0]
        break
print(key)