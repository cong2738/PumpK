'''
tc = [[[(lambda price,name:[int(price),name])(*(input().split()))] for j in range(int(input()))] for i in range(int(input()))]
for l in tc:
    [print(max(l,key=lambda x:x[0])[0][1])]
'''
ret = []
n=int(input())
for i in range(n):
    p=int(input())
    person = ["0",""]
    for i in range(p):
        newperson = input().split()
        if int(newperson[0])>=int(person[0]):
            person=newperson
    ret.append(person[1])
print(*ret,sep='\n')