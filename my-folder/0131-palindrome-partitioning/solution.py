class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.dfs(s, 0, [], 0)
        return self.res
    def dfs(self, s, start, t, k):
        if k == len(s):
            self.res.append(copy.deepcopy(t))
        
        for end in range(start, len(s)):
            sub_string = s[start:end+1]
            if self.isPalindrome(sub_string):
                t.append(sub_string)
                self.dfs(s, end+1,t, k + len(sub_string))
                t.pop()

    def isPalindrome(self, s):
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True



        
