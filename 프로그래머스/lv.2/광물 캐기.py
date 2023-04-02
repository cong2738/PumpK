def solution(picks, minerals):
    Fatigue = [
        {"diamond":1,"iron":1,"stone":1}, 
        {"diamond":5,"iron":1,"stone":1}, 
        {"diamond":25,"iron":5,"stone":1}, ]

    picks_num = sum(picks)
    picks = [0]*picks[0]+[1]*picks[1]+[2]*picks[2]

    m5 = sorted([minerals[5*i:5*i+5] for i in range(picks_num)],reverse=True,key=lambda x:sum(map(lambda i:Fatigue[2][i],x)))

    res = 0
    for i in range(picks_num):
        if not m5[i]: break
        res += sum(map(lambda minerals:Fatigue[picks[i]][minerals],m5[i]))

    return res