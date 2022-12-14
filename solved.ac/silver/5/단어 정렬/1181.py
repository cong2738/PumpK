n = int(input())
print(*sorted({input() for i in range(n)}, key = lambda x:[len(x),x]),sep = '\n')
