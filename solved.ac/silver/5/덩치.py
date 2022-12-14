person_list=[input() for i in range(int(input()))]
person_list.sort(reverse=True)
print(*person_list, sep='\n')