
n = int(input())
student = [list(map(int,input().split())) for i in range(n)]
mate = [[0]*n for i in range(n)]
for person in range(len(student)):
    for grade in range(5):
        for frend in range(len(student)):
            if student[person][grade] == student[frend][grade]:
                mate[person][frend] = 1
mate = [person.count(1) for person in mate]
print(1 + mate.index(max(mate)))
