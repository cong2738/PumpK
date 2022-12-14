def find_room(floor,room,num_of_guest):
    count = 0
    for R in range(room):
        for F in range(floor):
            count += 1
            if count == num_of_guest:
                return (F+1)*100 + R+1
    return (F+1)*100 + R+1
for i in range(int(input())):
    Room_number = find_room(*map(int,input().split()))
    print(Room_number)
