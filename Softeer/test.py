around = ((0,1),(1,0),(-1,0),(0,-1))
ahead_char = {(0,1):'v',(1,0):'>',(0,-1):'^',(-1,0):'<'}
a =['v', '>', '<', '^']
for xx,sss in zip(around,a):
    print(ahead_char[xx]==sss)