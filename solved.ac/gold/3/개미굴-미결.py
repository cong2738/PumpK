class Pumkp_trie:    
    def __init__(self,words): 
        self.set_trie(words)

    def set_trie(self,words):
        self.trie = dict()
        for word in words:
            current_dict = self.trie
            for letter in word:
                current_dict = current_dict.setdefault(letter, {})

    def triepush(self,word):
        if not self.trie: 
            self.set_trie(word)
            return
        current = self.trie
        for c in word:
            if c in current: 
                current = current[c]
                continue
            current = current.setdefault(c,{})
        current[None] = None
            
        
    def find(self,word):
        if not self.trie: return False
        current = self.trie
        for c in word:
            if c in current: current = current[c]
            else: return False
        return True

    def get(self): 
        return self.trie
import sys
from collections import deque
readline = sys.stdin.readline

def dfs(key:tuple[str],Route:str,current:dict,depth:int):    
    if not key: return
    res = '--'*depth + key
    print(res)
    visited[Route] = True
    for np in sorted(current.keys()): 
        if np and not key+' '+np in visited: dfs(np,key+' '+np,current[np],depth+1)

trie = Pumkp_trie([readline().split()[1:] for _ in range(int(readline()))])
개미굴 = trie.get()
for key in sorted(개미굴.keys()):
    visited = dict()
    dfs(key,key,개미굴[key],0)