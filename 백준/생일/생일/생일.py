n = int(input())
person = []
for i in range(n):
    name,day,month,year = input().split()    
    person.append([name,list(map(int,[year,month,day]))])
person.sort(key=lambda x:x[1])
on[0][0],sep='\n')