import math

buttons = [8,4,1]
push_time = 0
push = []
distance, time = map(int,input().split())
while distance != 0:
    bt_times = [math.inf,math.inf,math.inf]
    for bt in range(len(buttons)):
        bt_time = distance//buttons[bt]
        if bt_time <= time and distance%buttons[bt] == 0:
            bt_times = [math.inf,math.inf,math.inf]
            bt_times[bt] = bt_time
            break
        elif bt_time != 0:
            bt_times[bt] = bt_time
    mt = min(bt_times)
    bt = buttons[bt_times.index(mt)]
    push.append([push_time,bt])
    push_time += distance//bt
    distance %= bt
if push_time < time:
    for index in range(len(push)):
        push[index][0] += time - push_time
elif push_time > time:
    push = [[-1]]
for btdata in push:
    print(*btdata)