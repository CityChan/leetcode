class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        letter_dict = {}
        for i in s:
            if i in letter_dict:
                letter_dict[i]+=1
            else:
                letter_dict[i]=1
        count = 0
        flag = 0
        for i in letter_dict:
            count+=letter_dict[i]//2
            if letter_dict[i]%2==1:
                flag = 1
        return count*2+flag
        
