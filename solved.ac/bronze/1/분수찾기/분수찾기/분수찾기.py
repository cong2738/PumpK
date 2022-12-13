
x = int(input())
before,after,index = 0,0,0
while after < x:
    before=after
    index+=1
    after = int(index*(index+1)/2)
if index%2==0:
    print(str(index+x-after)+'/'+str(1+after-x))
else:
    print(str(1+after-x)+'/'+str(index+x-after))
