class Solution:
    def decodeString(self, s: str) -> str:
        nbr_stack = []
        str_stack = []
        current_nbr = 0
        current_str = ""
        res = ""
        for i in s:
            if i.isdigit():
                current_nbr = current_nbr*10+int(i)
            elif i == '[':
                nbr_stack.append(current_nbr)
                str_stack.append(current_str)
                current_nbr = 0
                current_str = ""
            elif i == ']':
                current_str = str_stack.pop()+nbr_stack.pop()*current_str
                # res+=current_str
                # current_str = ""
            else:
                current_str+=i
        return res+current_str
        
