def solution(a, b):
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    monthdata = [31,29,31,30,31,30,31,31,30,31,30,31]
    return day[(sum(monthdata[:a-1])+b-1)%7]
print(solution(1,1))
