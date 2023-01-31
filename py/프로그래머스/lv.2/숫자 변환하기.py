from collections import deque
def solution(s, e, d):
	cnt,q = {s:0},deque([s])
	move = lambda x:{x+d, x*2, x*3}
	while q:
		p = q.popleft()
		for np in move(p):
			if np > e or np in cnt: continue
			cnt[np] = cnt[p] + 1
			q.append(np)
	return cnt[e] if e in cnt else -1

print(solution(10,40,5))