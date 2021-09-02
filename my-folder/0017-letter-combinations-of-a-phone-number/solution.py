class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letter_dict = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno",
                      7: "pqrs", 8: "tuv", 9: "wxyz"}
        def recur(digits):
            if len(digits)==1:
                return list(letter_dict[int(digits)])
            if len(digits)==2:
                res = []
                for i in letter_dict[int(digits[0])]:
                    for j in letter_dict[int(digits[1])]:
                        res.append(i+j)
                return  res
            if len(digits)>2:
                res = []
                left_res = recur(digits[:-1])
                for i in left_res:
                    for j in letter_dict[int(digits[-1])]:
                        res.append(i+j)
                return res
        return recur(digits)
            
                

        
