import sys
readline = sys.stdin.readline
n,m = map(int,readline().split())
never_seen = set(readline().strip() for _ in range(n))
never_heard = set(readline().strip() for _ in range(m))
ret = sorted(never_seen & never_heard)
print(len(ret),*ret,sep='\n')