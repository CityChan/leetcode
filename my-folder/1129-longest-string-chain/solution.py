class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
#         def is_pred(s1, s2):
#             flag = 0
#             i = 0
#             j = 0
#             while i<len(s1) and j<len(s2):
#                 if s1[i]!=s2[j]:
#                     if flag==1:
#                         return False
#                     flag = 1
#                     j+=1
#                 else:
#                     i+=1
#                     j+=1
#             if ((flag==0) and i==len(s1) and j<len(s2)-1) or ((flag==1) and (i!=len(s1) or j!=len(s2))):
#                 return False
#             else:
#                 return True
            
#         if len(words)==1:
#             return True

        res = {}
        words = sorted(words, key = len)
        for w in words:
            now_max = 1
            for i in range(len(w)):
                # if len(w)==1:
                #     continue
                now_word = w[:i]+w[i+1:]
                if now_word in res:
                    now_max = max(now_max, res[now_word]+1)
            res[w]=now_max
        return max(res.values())
                                                          
