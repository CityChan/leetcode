class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        char_list = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        
        res = ""
        for i in range(len(char_list)):
            n = num//num_list[i]
            num = num-n*num_list[i]
            res+=char_list[i]*n
        return res

        
