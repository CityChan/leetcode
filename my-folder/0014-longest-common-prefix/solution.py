class Solution(object):
    # def longestCommonPrefix(self, strs):
    #     """
    #     :type strs: List[str]
    #     :rtype: str
    #     """
    #     if not strs:
    #         return ""
    #     shortest = min(strs,key=len)
    #     for i, ch in enumerate(shortest):
    #         for other in strs:
    #             if other[i] != ch:
    #                 return shortest[:i]
    #     return shortest 
    
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs = sorted(strs, key = len)
        shortest = strs[0]
        for i in range(len(shortest)):
            for s in strs[1:]:
                if s[i]!=shortest[i]:
                    return shortest[:i]
        return shortest
        
