sum, L = 0, []
for score in sorted(sorted([[int(input()), i] for i in range(1,9)], reverse=True)[:5], key=lambda x:x[1]):
    sum += score[0]
    L += [score[1]]
print(sum)
print(*L)