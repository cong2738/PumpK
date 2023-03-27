def solution(picks, minerals):
    scores = [
        {"diamond":3,"iron":2,"stone":1},
        {"diamond":25,"iron":5,"stone":1},
        {"diamond":5,"iron":2,"stone":1},
        {"diamond":1,"iron":1,"stone":1},        
    ]
    
    m5 = []
    answer = 0
    for i in range(0,len(minerals),5):
        m5.append(minerals[i:i+5])

    m5.sort(reverse=True, key=lambda x:sum(map(lambda i:scores[0][i],x)))
    print(m5)

    for _,line in m5:


    return answer

picks = [1, 3, 2]
minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
solution(picks,minerals)