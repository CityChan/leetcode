class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        i = 0
        while i<len(str1) and i<len(str2):
            if str1[i]==str2[i]:
                i+=1
            else:
                break
        j = i
        while j>0:
            if len(str1)%j!=0 or len(str2)%j!=0:
                j-=1
                continue
            flag = 0
            k = 0
            while k<len(str1):
                if str1[k]!=str1[k%j]:
                    flag = 1
                    break
                k+=1
            k = 0
            while k<len(str2):
                if str2[k]!=str1[k%j]:
                    flag = 1
                    break
                k+=1
            if flag == 1:
                j-=1
                continue
            else:
                break
        return str1[:j]
