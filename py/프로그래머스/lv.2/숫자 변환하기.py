from collections import deque
def solution(s, e, d):
	cnt = {s:0}
	q = deque([s])
	while q:
		p = q.popleft()
		for np in [p+d,p*2,p*3]:
			if np > e or np in cnt: continue
			cnt[np] = cnt[p] + 1
			q.append(np)
	return cnt[e] if e in cnt else -1

print(solution(10,40,5))