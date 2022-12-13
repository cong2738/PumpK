from itertools import permutations
def solution(n, k):
    return list(permutations([i + 1 for i in range(n)],n))[k-1]
print(*solution(3,5)[5-1],sep='\n')