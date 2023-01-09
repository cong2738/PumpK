def solution(today, terms, privacies):
    convert = [12*28,28,1]
    conv = lambda date: sum([num*con for num,con in zip(list(map(int,date.split('.'))),convert)])
    answer = []    
    today = conv(today)
    terms = {name:int(month)*28 for name,month in map(lambda s:s.split(),terms)}
    for i,(date,name) in enumerate(map(lambda s:s.split(),privacies)):
        date = conv(date)
        if today - date >= terms[name]: answer.append(i+1)
    return answer

print(
    solution(
        "2022.05.19",
        
        ["A 6", "B 12", "C 3"],
        
        ["2021.05.02 A", 
        "2021.07.01 B", 
        "2022.02.19 C", 
        "2022.02.20 C"]
        )
    )