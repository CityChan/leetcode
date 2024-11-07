class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.res = []
        self.track = []
        self.backtrack(s, 0, wordDict)
        return self.res

    def backtrack(self,s, i, wordDict):
        if i == len(s):
            self.res.append(" ".join(self.track))
            return 
        if i > len(s):
            return
        
        for word in wordDict:
            len_word = len(word)
            if i + len_word > len(s):
                continue
            sub_str = s[i: i + len_word]
            if sub_str != word:
                continue
            self.track.append(sub_str)
            self.backtrack(s, i + len_word, wordDict)
            self.track.pop()
            

