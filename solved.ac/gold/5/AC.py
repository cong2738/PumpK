import sys
from collections import deque
readline = sys.stdin.readline

for _ in range(int(readline())):
    string:str = readline().rstrip()
    if int(readline()): 
        nums:deque = deque(readline().strip('[]\n').split(','))
    else: 
        readline()
        nums:deque = deque([])
    cursor = 1
    for cmd in string:
        if cmd == 'R': cursor = ~cursor
        elif cmd == 'D' and nums: 
            nums.popleft() if cursor == 1 else nums.pop()
        else: 
            res = 'error'
            break
    else: 
        res = '[' + ','.join(nums if cursor == 1 else reversed(nums)) + ']'
    print(res)