security,bigdata = 0,0
N= int(input())
line = input()
index = 0
while(index<len(line)):
    if line[index] == 's':
        index += 8
        security += 1
    elif line[index] == 'b':
        index += 7
        bigdata += 1
if security == bigdata: print("bigdata? security!")
else: print("security!" if security > bigdata else "bigdata?")