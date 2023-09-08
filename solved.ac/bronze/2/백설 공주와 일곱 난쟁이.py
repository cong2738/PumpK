import sys
readline = sys.stdin.readline

hat = [int(readline()) for _ in range(9)]
sum_h = sum(hat)

def search_out(hat)->set:
    for i in range(9):
        for j in range(i+1,9):
            if sum_h - hat[i] - hat[j] == 100: 
                return {hat[i],hat[j]}
    return {}

suspect = search_out(hat)
for gnome in hat:
    if gnome in suspect:continue
    print(gnome)