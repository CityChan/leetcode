class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        bool_res_list = [True]
        for i in range(len(s)):
            flag = 0
            for w in wordDict:
                if i-len(w)+1<0:
                    continue
                if s[i-len(w)+1:i+1]==w and bool_res_list[i-len(w)+1]:
                    flag = 1
                    break
            if flag==1:
                bool_res_list.append(True)
            else:
                bool_res_list.append(False)
        return bool_res_list[-1]
        
