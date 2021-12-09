class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        res_dict = {}
        for i in cpdomains:
            temp = i.split(" ")
            tt = temp[1].split(".")
            temp_s = ""
            for j in range(len(tt)-1, -1, -1):
                if j==len(tt)-1:
                    temp_s = tt[j]+temp_s
                else:
                    temp_s = tt[j]+"."+temp_s
                    
                if temp_s not in res_dict:
                    res_dict[temp_s]=int(temp[0])
                else:
                    res_dict[temp_s]+=int(temp[0])
                        
        return [str(res_dict[i])+" "+i for i in res_dict]
            
