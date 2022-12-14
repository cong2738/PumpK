line=list(map(int,input().split()))
while line != [0, 0, 0]:
    line.sort()
    print('right' if line[0]**2 + line[1]**2 == line[2]**2 else 'wrong')
    line=list(map(int,input().split()))
