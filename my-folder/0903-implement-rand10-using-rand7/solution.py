# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        temp = 41
        while temp>40:
            temp = (rand7()-1)*7+rand7()
        return temp%10+1

    
    
    
    
