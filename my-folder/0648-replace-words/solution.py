class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for i,word in enumerate(dictionary):
            trie.insert(word, i)
        ans = []
        for word in sentence.split(' '):
            idx = trie.search(word)
            ans.append(dictionary[idx] if idx!= -1 else word)
        return " ".join(ans)
class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.ref = -1
    
    def insert(self, w, i):
        node = self
        for c in w:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.ref = i

    def search(self, w):
        node = self
        for c in w:
            print(c)
            idx = ord(c) - ord('a')
            print(idx)
            if node.children[idx] is None:
                return -1
            node = node.children[idx]
            if node.ref != -1:
                return node.ref
        return -1




