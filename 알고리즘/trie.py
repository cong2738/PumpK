#trie(트라이): 여러개의 문자열을 기존 입력을 기반으로 빠르게 탐색하기 위한 트리구조의 자료구조( 메모리를 많이먹는대신 O(log(N)로탐색속도가 매우빠르다. )
class Pumkp_trie:    
    def __init__(self,*words): 
        self.triepush(*words)
    
    #데이터 접근 편의를 위해 각 노드와 자식 노드관계는 해시맵을 사용한다.
    def triepush(self,*words):
        self.trie = dict()
        for word in set(words):
            current_dict = self.trie
            for letter in word:
                current_dict = current_dict.setdefault(letter, {})
            current_dict[None] = None
    
    def find(self,word):
        current = self.trie
        for c in word:
            if c in current: current = current[c]
            else: return False
        return True

    def get(self): 
        return self.trie

import sys
readline = sys.stdin.readline
N,M = map(int,readline().split())
my_trie = Pumkp_trie(*{readline().rstrip() for _ in range(N)})
for _ in range(M):
    my_trie.triepush(readline().rstrip())
my_trie.triepush(readline().rstrip())
print(my_trie.find(readline().rstrip()))