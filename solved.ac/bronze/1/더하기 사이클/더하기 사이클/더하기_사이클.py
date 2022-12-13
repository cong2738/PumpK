n = input()
if(int(n)<10):
    n='0'+n
m = n
count = 0
while True:
    count+=1
    n = n[-1] + str(sum(map(int,list(n))))[-1]    
    if n == m: break
print(count)