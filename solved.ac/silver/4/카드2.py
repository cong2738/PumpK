from collections import deque
q = deque(range(int(input())))
while len(q):
    num = q.popleft()
    q.rotate(-1)
print(num + 1)
