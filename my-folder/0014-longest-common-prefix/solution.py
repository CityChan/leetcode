class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in strs:
            if i=="":
                return ""
        if len(strs)==1:
            return strs[0]
        
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if len(strs[j])<=i or strs[j][i]!=strs[0][i]:
                    break
                    
            if j<len(strs)-1 or \
                (j==len(strs)-1 and (len(strs[j])<=i or strs[j][i]!=strs[0][i])):
                break
        if i==len(strs[0])-1 and j==len(strs)-1 and len(strs[j])>i and strs[j][i]==strs[0][i]:
            i+=1
                
        if i==0:
            for j in range(1, len(strs)):
                if strs[j][0]!=strs[0][0]:
                    return ""
            return strs[0][0]
        else:
            return strs[0][:i]
        
                    
        
