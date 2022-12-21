n = int(input())
people = sorted(list(map(int,input().split())))
print(sum([sum(people[:i+1]) for i in range(n)]))