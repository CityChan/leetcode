class Solution:
    def reverseWords(self, s: str) -> str:
        s_splited = s.split(" ")
        s_splited.reverse()
        ans = ""
        for word in s_splited:
            if len(word) == 0:
                continue
            ans = ans + word + " "
        return ans[:-1]
