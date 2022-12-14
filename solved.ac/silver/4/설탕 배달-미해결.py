sugar, num, bags = int(input()), 0, [5,3]
for bag in bags:
    num += sugar//bag
    sugar %= bag
    print(sugar)
if sugar ==0 : print(num)
else : print(-1)