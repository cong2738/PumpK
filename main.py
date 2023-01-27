import csv
cashCube = {'블랙 큐브','레드 큐브'}
f = open('Maple_API_Cube_utf-8.csv','r',encoding='UTF8')
rdr = list(csv.reader(f))
res = [line for line in rdr if line[2] in cashCube]
print(res)
print('end')