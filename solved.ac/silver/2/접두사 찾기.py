import sys
readline = sys.stdin.readline

def make_trie(words:set):
    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict[None] = None
    return root

res = 0
N,M = map(int,readline().split())
word_trie = make_trie({readline().rstrip() for _ in range(N)})
for _ in range(M):
    current = word_trie
    for c in readline().rstrip():
        if c in current: current = current[c]
        else: break
    else: res += 1

print(res)