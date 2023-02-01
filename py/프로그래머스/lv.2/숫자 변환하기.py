from collections import deque
def solution(s:int, e:int, d:int):
	cnt,q = {s:0},deque([s])
	move = lambda x:{x+d, x*2, x*3}
	while q:
		p = q.popleft()
		for np in move(p):
			if np > e or np in cnt: continue
			cnt[np] = cnt[p] + 1
			q.append(np)
	return cnt[e] if e in cnt else -1
print(solution(2,5,4))

def solution2(s:int, e:int, d:int):
	cnt = {s:0}
	for i in range(s+1,e+1):
		b = [cnt[int(n)] for n in (i - d,i / 2,i / 3) if n == int(n) and int(n) in cnt]
		if b: cnt[i] = min(b) + 1
	return cnt[e] if e in cnt else -1
print(solution2(10, 40, 5))