class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        i = 0
        while i < len(letters):
            if letters[i]<=target:
                i+=1
            else:
                break
        if i==len(letters):
            return letters[0]
        else:
            return letters[i]
        
