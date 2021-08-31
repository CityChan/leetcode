class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        idx = {c:i for i, c in enumerate(order)}
        for pre in range(len(words)-1):
            for i in range(min(len(words[pre]), len(words[pre+1]))):
                if idx[words[pre][i]]<idx[words[pre+1][i]]:
                    print("yes")
                    break
                elif idx[words[pre][i]]>idx[words[pre+1][i]]:
                    return False
                else:
                    if i == len(words[pre+1])-1 and i != len(words[pre])-1:
                        return False
        return True
                    
                        
            
        
