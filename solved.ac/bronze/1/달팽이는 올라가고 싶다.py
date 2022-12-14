import math
a,b,v = map(int,input().split())
date = 0
date = (v-a)/(a - b)
print(math.ceil(date) + 1)