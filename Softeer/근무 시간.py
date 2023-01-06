import sys
readline = sys.stdin.readline
def time_to_minute(string):
    hour,minute = map(int,string.split(':'))
    minute += hour*60
    return minute

worktime = 0
for _ in range(5):
    start,end = map(time_to_minute,readline().split())
    worktime += end - start
print(worktime)