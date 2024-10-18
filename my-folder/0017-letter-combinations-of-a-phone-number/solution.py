class Solution:
    
    def __init__(self):
        self.res = []
        self.sb = []
        self.mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return self.res
        self.backtrack(digits, 0)
        return self.res
        
    def backtrack(self, digits, start):
        if len(self.sb) == len(digits):
            self.res.append("".join(self.sb))
            return
        digit = int(digits[start])
        letters = self.mapping[digit]
        for letter in letters:
            self.sb.append(letter)
            self.backtrack(digits, start + 1)
            self.sb.pop()
        return
                
