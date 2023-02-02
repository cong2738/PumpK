'''
trie(트라이): 여러개의 문자열을 기존 입력을 기반으로 빠르게 탐색하기 위한 트리구조의 자료구조( 메모리를 많이먹는대신 O(log(N)로탐색속도가 매우빠르다. )
데이터 접근 편의를 위해 각 노드와 자식 노드관계는 해시맵을 사용한다.
'''
class Pumkp_trie:    
    def __init__(self,words): 
        self.set_trie(words)
    #words는 [[a,c],[b,a],[c,e],[e,d]] 같은 형태로 들어간다
    def set_trie(self,words:iter[iter]):
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
            if not c in current: current[c] = dict()
            current = current[c]
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